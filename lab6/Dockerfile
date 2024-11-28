# Вибираємо базовий образ з Python
FROM python:3.9-slim

# Встановлюємо необхідні пакети
RUN apt-get update && apt-get install -y python3-pip

# Створюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файли програми і тестів до контейнера
COPY . /app

# Встановлюємо залежності (якщо у тебе є requirements.txt)
# RUN pip install -r requirements.txt

# Команда для запуску програми
CMD ["python3", "-m", "unittest", "discover", "-s", "."]

# Для запуску програми (у випадку запуску не тестів, а основної програми)
# CMD ["python3", "lab2.py"]
