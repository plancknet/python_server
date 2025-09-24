FROM python:3.12-slim

WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY app.py .

EXPOSE 8000

# Inicia com Gunicorn (produção)
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8000", "app:app"]
