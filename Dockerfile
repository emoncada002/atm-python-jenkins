FROM app-python-base:latest
COPY . /app
CMD ["python", "main.py"]

# Versión de producción optimizada con Docker y Jenkins - Fase 3
