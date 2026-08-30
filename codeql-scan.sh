#!/usr/bin/env bash

# Uso: ./codeql-scan.sh /caminho/para/o/repositorio

set -euo pipefail

TARGET_DIR="${1:-}"
if [ -z "$TARGET_DIR" ]; then
  echo "[ERRO] Informe o diretório do repositório."
  echo "Uso: $0 /caminho/para/o/repositorio"
  exit 1
fi

TARGET_DIR="$(realpath "$TARGET_DIR")"

CODEQL_VERSION=$(codeql version --format=terse 2>/dev/null || codeql version | head -1)

echo "[INFO] CodeQL CLI: $CODEQL_VERSION"

WORK_DIR="$(pwd)/codeql-output"
DB_DIR="$WORK_DIR/database"
RESULTS_DIR="$WORK_DIR/results"
PYTHON_LIST="$WORK_DIR/python_files.txt"

mkdir -p "$WORK_DIR" "$RESULTS_DIR"

find "$TARGET_DIR" -type f -name "*.py" \
  ! -path "*/.git/*" \
  ! -path "*/node_modules/*" \
  ! -path "*/.venv/*" \
  ! -path "*/venv/*" \
  ! -path "*/__pycache__/*" \
  ! -path "*/migrations/*" \
  | sort > "$PYTHON_LIST"

PY_COUNT=$(wc -l < "$PYTHON_LIST")
echo "[INFO] $PY_COUNT arquivo(s) .py encontrado(s):"
cat "$PYTHON_LIST"

if [ "$PY_COUNT" -eq 0 ]; then
  echo "[AVISO] Nenhum arquivo .py encontrado. Encerrando."
  exit 0
fi

#etapa 2

# Remove database anterior se existir
[ -d "$DB_DIR" ] && rm -rf "$DB_DIR"

codeql database create "$DB_DIR" \
  --language=python \
  --source-root="$TARGET_DIR" \
  --overwrite \
  --threads=0


#etapa 3

# Função auxiliar: roda uma query e salva o SARIF individual
run_query() {
  local CWE="$1"
  local QUERY_PATH="$2"
  local LABEL="$3"
  local OUT_FILE="$RESULTS_DIR/${CWE}_${LABEL}.sarif"

  echo ""
  echo "[→] $CWE · $LABEL"

  if codeql database analyze "$DB_DIR" \
    "$QUERY_PATH" \
    --format=sarif-latest \
    --output="$OUT_FILE" \
    --threads=0 \
    --sarif-add-query-help \
    2>&1; then
    echo "    ✔ Concluído → $OUT_FILE"
  else
    echo "    ✘ Falha ao executar: $QUERY_PATH"
  fi
}

# ── CWE-20 · Improper Input Validation ──────────────────────
run_query "CWE-020" "python/ql/src/Security/CWE-020/OverlyLargeRange.ql"                     "OverlyLargeRange"
run_query "CWE-020" "python/ql/src/Security/CWE-020/IncompleteHostnameRegExp.ql"             "IncompleteHostnameRegExp"
run_query "CWE-020" "python/ql/src/Security/CWE-020/IncompleteUrlSubstringSanitization.ql"   "IncompleteUrlSubstringSanitization"
run_query "CWE-020" "python/ql/src/Security/CWE-020/CookieInjection.ql"                      "CookieInjection"
run_query "CWE-020" "python/ql/src/Security/CWE-020/BadTagFilter.ql"                         "BadTagFilter"

# ── CWE-22 · Path Traversal ─────────────────────────────────
run_query "CWE-022" "python/ql/src/Security/CWE-022/PathInjection.ql"                        "PathInjection"
run_query "CWE-022" "python/ql/src/Security/CWE-022/TarSlip.ql"                              "TarSlip"

# ── CWE-78 · OS Command Injection ────────────────────────────
run_query "CWE-078" "python/ql/src/Security/CWE-078/CommandInjection.ql"                     "CommandInjection"
run_query "CWE-078" "python/ql/src/Security/CWE-078/ShellCommandConstructedFromInput.ql"     "ShellCommandConstructedFromInput"

# ── CWE-79 · Cross-Site Scripting ────────────────────────────
run_query "CWE-079" "python/ql/src/Security/CWE-079/ReflectedXss.ql"                         "ReflectedXss"
run_query "CWE-079" "python/ql/src/Security/CWE-079/HttpResponseSplitting.ql"                "HttpResponseSplitting"
run_query "CWE-079" "python/ql/src/Security/CWE-079/Jinja2WithoutEscaping.ql"                "Jinja2WithoutEscaping"

# ── CWE-89 · SQL Injection ───────────────────────────────────
run_query "CWE-089" "python/ql/src/Security/CWE-089/SqlInjection.ql"                         "SqlInjection"

# ── CWE-94 · Code Injection ──────────────────────────────────
run_query "CWE-094" "python/ql/src/Security/CWE-094/CodeInjection.ql"                        "CodeInjection"
run_query "CWE-094" "python/ql/src/Security/CWE-094/UseOfInput.ql"                           "UseOfInput"

# ── CWE-352 · Cross-Site Request Forgery ────────────────────
run_query "CWE-352" "python/ql/src/Security/CWE-352/CSRFProtection.ql"                       "CSRFProtection"

# ── CWE-502 · Deserialization of Untrusted Data ──────────────
run_query "CWE-502" "python/ql/src/Security/CWE-502/UnsafeDeserialization.ql"                "UnsafeDeserialization"

# ── CWE-798 · Use of Hard-coded Credentials ──────────────────
run_query "CWE-798" "python/ql/src/Security/CWE-798/HardcodedCredentials.ql"                 "HardcodedCredentials"

# ── CWE-918 · Server-Side Request Forgery ────────────────────
run_query "CWE-918" "python/ql/src/Security/CWE-918/FullServerSideRequestForgery.ql"         "FullSSRF"
run_query "CWE-918" "python/ql/src/Security/CWE-918/PartialServerSideRequestForgery.ql"      "PartialSSRF"


echo "[INFO] Resultados SARIF salvos em: $RESULTS_DIR"
echo "[INFO] Arquivos gerados:"
ls -1 "$RESULTS_DIR"/*.sarif 2>/dev/null || echo "  (nenhum arquivo gerado)"
