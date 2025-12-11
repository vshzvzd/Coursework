# Базовый образ Python
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файл зависимостей первым
COPY requirements.txt .

# Устанавливаем зависимости с доверенными хостами (на случай проблем с сетью)
RUN pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

# Копируем остальные файлы проекта
COPY . .

# Открываем порт для Flask
EXPOSE 5000

# Команда запуска приложения
CMD ["python", "app.py"]
