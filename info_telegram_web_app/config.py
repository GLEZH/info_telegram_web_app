import os

BOT_TOKEN = os.getenv('BOT_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
WEBAPP_HOST = os.getenv('WEBAPP_HOST', '0.0.0.0')
WEBAPP_PORT = int(os.getenv('WEBAPP_PORT', 8080))
