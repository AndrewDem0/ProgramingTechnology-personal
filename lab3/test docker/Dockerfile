FROM alpine

# Встановлення Python3 та pip
RUN apk add --update python3 py3-pip

# Встановлення віртуального середовища
RUN python3 -m venv /venv

# Активація віртуального середовища і встановлення Flask
RUN /venv/bin/pip install flask

# Копіювання всіх файлів в контейнер
COPY . /app

# Встановлення робочої директорії
WORKDIR /app

# Використання ENTRYPOINT для запуску Python з активованим віртуальним середовищем
ENTRYPOINT ["/venv/bin/python"]

# Вказання команди для запуску Flask додатку
CMD ["app.py"]