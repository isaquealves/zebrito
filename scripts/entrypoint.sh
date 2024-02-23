#!/usr/bin/env sh
set -e

exec uvicorn zebrito.main:app  --host 0.0.0.0 --port 8080 --loop uvloop --timeout-keep-alive 300 --http h11