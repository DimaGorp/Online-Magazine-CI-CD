# Используйте официальный образ Python
FROM python:3.12.2

# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости проекта
WORKDIR /app
RUN pip install -r requirements.txt

# Копируем остальной код проекта в контейнер
COPY . /app

# Запускаем приложение
CMD ["python", "manage.py", "runserver"]
