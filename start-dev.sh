#!/bin/bash

echo "Running Alembic migrations..."
alembic upgrade head

if [ $? -eq 0 ]; then
  echo "Alembic migrations completed successfully."
  echo "Starting Uvicorn server..."
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
  echo "Error running Alembic migrations. Exiting."
  exit 1
fi