FROM python:3.11-slim

WORKDIR /app

# Копируем файл зависимостей
COPY app/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY app/ .

# Создаем пользователя для безопасности
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

# Открываем порт
EXPOSE 5000

# Команда запуска
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "main:app"]
