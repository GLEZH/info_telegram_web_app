FROM python:3.12-slim

WORKDIR /info_telegram_web_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "info_telegram_web_app/main.py"]
