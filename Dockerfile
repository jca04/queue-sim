# ---------- Etapa base ----------
FROM python:3.11-slim AS base

# Configuración del entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y build-essential libpq-dev && apt-get clean

# Copiar requirements y dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer puerto
EXPOSE 8000

# Comando de ejecución
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
