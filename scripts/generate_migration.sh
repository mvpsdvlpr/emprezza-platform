#!/bin/bash
# Script para generar una nueva migración de forma profesional

if [ -z "$1" ]; then
  echo "❌ Error: Debes ingresar un nombre para la migración."
  echo "✅ Ejemplo: ./generate_migration.sh add_user_table"
  exit 1
fi

echo "🚀 Generando nueva migración: $1"
alembic revision --autogenerate -m "$1"
