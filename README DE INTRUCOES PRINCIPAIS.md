# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Linux Incident Response Triage Collector

**Repositório Oficial:** `https://github.com/Techdimbr/linux-ir-triage-collector`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Base Canônica Homologada — Pronto para Expansão de Funções  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Linux Incident Response Triage Collector
- **Identificador (Slug):** `linux-ir-triage-collector`
- **Categoria:** Forense Computacional & Resposta a Incidentes (Blue Team)
- **Stack Tecnológica:** Bash nativo (POSIX), `ss`, `ps`, `lsof`, `ip`, `sha256sum`, ISO/IEC 27037, RFC 3227
- **Objetivo Central:** Fornecer um script determinístico de triagem forense live-response para servidores Linux sob suspeita de intrusão, coletando dados voláteis com preservação da cadeia de custódia e selo criptográfico SHA-256.

### Casos de Uso Reais
1. **Triagem em Caso de Alerta do EDR/SIEM:** Coleta instantânea de processos e conexões ao detectar atividade maliciosa.
2. **Identificação de Shell Reversa e C2:** Detecção de processos ocultos com conexões TCP estabelecidas para IPs externos suspeitos.
3. **Preservação de Evidência para Ação Judicial:** Geração de pacote inviolável com manifesto e timestamps militares.

---

## 2. Estrutura dos Módulos em `03_APLICACAO/src/`

```text
03_APLICACAO/src/
├── triage_collector.sh                # Script principal de coleta forense volátil (POSIX Bash)
├── parser.py                          # Parser e validador de manifesto de integridade da coleta
└── modules/
    ├── 01_network_sockets.sh          # Coleta de sockets ativos, escutas e rotas
    ├── 02_process_tree.sh             # Coleta de árvore de processos, variáveis de ambiente e cwd
    └── 03_users_and_logins.sh         # Coleta de sessões ativas (w, who, lastlog, wtmp)
```

---

## 3. Guia Operacional para o Desenvolvedor

1. **Bootstrap do Ambiente:**
   ```bash
   ./iniciar.sh
   ```
2. **Executar Testes Unitários do Validador de Evidências:**
   ```bash
   python3 -m unittest discover 03_APLICACAO/tests
   ```
3. **Auditar Integridade Criptográfica dos Arquivos:**
   ```bash
   ./00_AUDITORIA/verificar_integridade.sh --gerar
   ```

---

## 4. Diretrizes e Regras de Negócio da Função (Para Preenchimento)
<!-- ÁREA DESTINADA À ESPECIFICAÇÃO DE NOVOS COLETORES FORENSES -->
- [x] Coleta padronizada de ordem de volatilidade (sockets -> processos -> rotas);
- [x] Geração automática de manifesto `manifest_sha256.txt` assinado;
- [ ] Módulo de extração de histórico de comandos (`.bash_history`) sem alterar timestamps mtime/atime;
- [ ] Compactação do pacote de evidências com tar gzip e cifragem opcional com GPG.
