# Используем базовый образ Python
FROM python:3.12.2

#  Устанавливаем рабочие директории
WORKDIR /store

# Копируем зависимости и устанавливаем их
COPY requirements.txt /store/
RUN pip install -r requirements.txt

# Копируем весь код проекта
COPY . .

# Открываем порт 8080 для доступа к приложению
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
