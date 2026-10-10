# 🏛️ README DE INSTRUÇÕES PRINCIPAIS — Linux Incident Response Triage Collector

**Repositório Oficial:** `https://github.com/Techdimbr/linux-ir-triage-collector`  
**Classificação:** Projeto de Referência Técnica Corporativa (Padrão Open-Core)  
**Doutrina de Engenharia:** Kether_1 · Central de Tecnologia TECHDIM  
**Status Atual:** Estrutura Base Canônica Homologada — Aguardando Desenvolvimento da Função  
**Website Institucional:** https://techdimbr.github.io/techdimbr/  
**Licença:** MIT Corporate  

---

## 1. Identificação e Propósito do Projeto
- **Nome Comercial:** Linux Incident Response Triage Collector
- **Identificador (Slug):** `linux-ir-triage-collector`
- **Categoria:** Forense Computacional & Resposta a Incidentes (Blue Team)
- **Stack Tecnológica:** Bash nativo (POSIX), ss, ps, lsof, ip, SHA-256
- **Objetivo Central:** Coletor de triagem forense live-response volátil para ambientes Linux em conformidade com ISO/IEC 27037. Extrai conexões de rede ativas, processos em execução, sockets e hashes de memória preservando a cadeia de custódia.

### Principais Casos de Uso Previstos
- Coleta rápida e padronizada de evidências voláteis em servidores Linux sob suspeita de comprometimento
- Preservação rigorosa da ordem de volatilidade sem alteração indevida de metadados do sistema
- Geração automatizada de manifesto de custódia com hashes SHA-256 de todos os artefatos coletados

---

## 2. Estrutura Operacional Canônica
Este repositório foi construído sobre a arquitetura canônica **PRJ-TECHDIM-PUBLIC-v1.0.0**:
- `00_AUDITORIA/`: Verificação criptográfica de integridade SHA-256 (`./00_AUDITORIA/verificar_integridade.sh`).
- `01_SOBRE_O_PROJETO/`: Documentação de requisitos, casos de uso e roadmap de desenvolvimento.
- `02_COMO_USAR/`: Procedimentos operacionais padrão (SOP), pré-requisitos e configurações.
- `03_APLICACAO/`: Núcleo de código (`src/`) e suite de testes automatizados (`tests/`).
- `04_INTELIGENCIA_DE_DESENVOLVIMENTO/`: Decisões de arquitetura (ADRs) e regras de contexto para agentes de IA.
- `05_VERSOES/`: Controle semântico de versões (`CHANGELOG.md`).
- `06_MIDIA/`: Material de apresentação executiva e ficha técnica.

---

## 3. Instruções Iniciais para Início do Desenvolvimento
Quando for iniciar o desenvolvimento da função específica:
1. **Ativação e Validação Inicial:**
   ```bash
   ./iniciar.sh
   ```
   *O bootstrap verificará o ambiente Debian/Linux, dependências e ativará os pre-commit hooks de proteção Zero Leaks.*

2. **Implementação do Core:**
   - Codifique a lógica da solução dentro do diretório `03_APLICACAO/src/`.
   - Mantenha o código modular, desacoplado e documentado.

3. **Criação e Execução de Testes:**
   - Escreva testes unitários e de integração em `03_APLICACAO/tests/`.
   - Valide a execução com:
     ```bash
     python3 -m unittest discover 03_APLICACAO/tests
     ```

4. **Auditoria de Integridade Criptográfica:**
   - Antes de efetuar novos commits de versão, atualize o manifesto SHA-256 executando:
     ```bash
     ./00_AUDITORIA/verificar_integridade.sh --gerar
     ```

---

## 4. Diretrizes e Regras de Negócio a Preencher
<!-- PREENCHA ESTA SEÇÃO COM AS DIRETRIZES ESPECÍFICAS DA FUNÇÃO QUANDO FOR INICIAR O DESENVOLVIMENTO -->
> **[ESPAÇO RESERVADO PARA DETALHAMENTO DA FUNÇÃO]**
> - Inserir aqui os casos de uso detalhados;
> - Inserir aqui parâmetros de entrada, saída e esquemas de dados;
> - Inserir requisitos específicos de bibliotecas e integração de APIs externas;
> - Inserir regras de segurança específicas para o ambiente de execução.
