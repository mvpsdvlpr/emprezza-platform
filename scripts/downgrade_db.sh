#!/bin/bash
# Script para revertir la última migración (opcional)

echo "⚠️ Revirtiendo última migración (downgrade -1)..."
alembic downgrade -1
