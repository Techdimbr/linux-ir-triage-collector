#!/bin/sh
# ==============================================================================
# TECHDIM - Linux Incident Response Triage Collector
# Coleta determinística de evidências voláteis em conformidade com ISO/IEC 27037
# ==============================================================================

set -e

OUTPUT_DIR="${1:-/tmp/techdim_ir_triage_$(date +%Y%m%d_%H%M%S)}"
mkdir -p "$OUTPUT_DIR"

echo "========================================================================"
echo "🚨 TECHDIM BLUE TEAM - INITIATING FORENSIC LIVE TRIAGE COLLECTION"
echo "Target Directory: $OUTPUT_DIR"
echo "Timestamp (UTC) : $(date -u)"
echo "========================================================================"

# 1. Informações básicas de tempo e uptime
echo "[1/4] Coletando carimbo temporal e uptime..."
date -u > "$OUTPUT_DIR/01_timestamp_utc.txt"
uptime > "$OUTPUT_DIR/01_uptime.txt"
uname -a > "$OUTPUT_DIR/01_kernel_uname.txt"

# 2. Conexões de rede ativas e sockets (ss / netstat)
echo "[2/4] Coletando conexões de rede e portas abertas..."
if command -v ss >/dev/null 2>&1; then
    ss -tulpn > "$OUTPUT_DIR/02_network_sockets.txt" 2>&1 || true
fi
if command -v ip >/dev/null 2>&1; then
    ip route > "$OUTPUT_DIR/02_network_routes.txt" 2>&1 || true
    ip neigh > "$OUTPUT_DIR/02_arp_cache.txt" 2>&1 || true
fi

# 3. Processos em execução (ps)
echo "[3/4] Coletando árvore de processos e comandos..."
ps auxf > "$OUTPUT_DIR/03_processes_tree.txt" 2>&1 || ps -ef > "$OUTPUT_DIR/03_processes_tree.txt" 2>&1

# 4. Geração do manifesto de cadeia de custódia com SHA-256
echo "[4/4] Gerando manifesto de custódia criptográfico SHA-256..."
cd "$OUTPUT_DIR"
sha256sum * > manifest_sha256.txt 2>/dev/null || true

echo "========================================================================"
echo "✓ Coleta finalizada com sucesso!"
echo "Manifesto inviolável gravado em: $OUTPUT_DIR/manifest_sha256.txt"
echo "========================================================================"
