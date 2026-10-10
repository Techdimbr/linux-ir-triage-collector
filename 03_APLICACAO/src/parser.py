#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de Cadeia de Custódia Forense
Verifica integridade de artefatos coletados contra o manifesto manifest_sha256.txt.
"""

import sys
import hashlib
from pathlib import Path
from typing import Dict, Tuple

def calcular_sha256(caminho: Path) -> str:
    """Calcula o hash SHA-256 de um arquivo."""
    hasher = hashlib.sha256()
    with open(caminho, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def validar_manifesto_custodia(diretorio: Path) -> Tuple[int, int, Dict[str, bool]]:
    """Valida se todos os arquivos listados no manifesto conferem com o hash no disco."""
    manifesto_path = diretorio / "manifest_sha256.txt"
    if not manifesto_path.exists():
        return 0, 1, {"manifest_sha256.txt": False}
        
    sucessos = 0
    falhas = 0
    status = {}
    
    with open(manifesto_path, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha or "manifest_sha256.txt" in linha:
                continue
            partes = linha.split(None, 1)
            if len(partes) == 2:
                hash_esperado, nome_arquivo = partes
                arquivo_path = diretorio / nome_arquivo.strip()
                if arquivo_path.exists() and calcular_sha256(arquivo_path) == hash_esperado:
                    sucessos += 1
                    status[nome_arquivo] = True
                else:
                    falhas += 1
                    status[nome_arquivo] = False
                    
    return sucessos, falhas, status

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 parser.py <diretorio_da_coleta>")
        sys.exit(1)
        
    pasta = Path(sys.argv[1])
    sucessos, falhas, status = validar_manifesto_custodia(pasta)
    
    print("=" * 65)
    print("🛡️  TECHDIM FORENSICS - VERIFICAÇÃO DE CUSTÓDIA ISO/IEC 27037")
    print("=" * 65)
    for arq, ok in status.items():
        icone = "✅" if ok else "❌"
        print(f"{icone} {arq:<35} : {'INTEGRO' if ok else 'VIOLADO / INEXISTENTE'}")
    print("-" * 65)
    print(f"Total: {sucessos} íntegros, {falhas} falhas.")
    sys.exit(0 if falhas == 0 else 1)

if __name__ == "__main__":
    main()
