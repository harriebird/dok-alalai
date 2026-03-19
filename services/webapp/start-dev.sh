#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

until pg_isready -h db -p 5432 > /dev/null 2>&1; do
  echo "Waiting for the PostgreSQL server..."
  sleep 1
done

alembic upgrade head

fastapi dev app/main.py --host 0.0.0.0
