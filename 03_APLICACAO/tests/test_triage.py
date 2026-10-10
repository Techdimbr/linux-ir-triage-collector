#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o validador de cadeia de custódia do Linux IR Triage Collector.
"""

import unittest
import tempfile
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from parser import validar_manifesto_custodia, calcular_sha256

class TestForensicTriageParser(unittest.TestCase):
    def test_validacao_manifesto_integro(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            pasta = Path(tmpdir)
            arq1 = pasta / "01_teste.txt"
            arq1.write_text("Evidencia forense pura", encoding="utf-8")
            hash1 = calcular_sha256(arq1)
            
            manifesto = pasta / "manifest_sha256.txt"
            manifesto.write_text(f"{hash1}  01_teste.txt\n", encoding="utf-8")
            
            sucessos, falhas, status = validar_manifesto_custodia(pasta)
            self.assertEqual(sucessos, 1)
            self.assertEqual(falhas, 0)
            self.assertTrue(status["01_teste.txt"])

    def test_validacao_manifesto_corrompido(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            pasta = Path(tmpdir)
            arq1 = pasta / "01_teste.txt"
            arq1.write_text("Evidencia forense pura", encoding="utf-8")
            
            manifesto = pasta / "manifest_sha256.txt"
            manifesto.write_text("hash_invalido_falso  01_teste.txt\n", encoding="utf-8")
            
            sucessos, falhas, status = validar_manifesto_custodia(pasta)
            self.assertEqual(sucessos, 0)
            self.assertEqual(falhas, 1)
            self.assertFalse(status["01_teste.txt"])

if __name__ == "__main__":
    unittest.main()
