#!/bin/bash
# Script para aplicar todas las migraciones pendientes

echo "🚀 Aplicando migraciones (upgrade head)..."
alembic upgrade head
