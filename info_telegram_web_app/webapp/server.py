from aiohttp import web
from jinja2 import Environment, FileSystemLoader
from app.database import AsyncSessionLocal
from app.models import User, Person
from app.config import WEBAPP_HOST, WEBAPP_PORT
import aiohttp_jinja2
import aiohttp
import jwt  # Для токенов

JWT_SECRET = 'your_jwt_secret'  # Замените на ваш секретный ключ

routes = web.RouteTableDef()

@aiohttp_jinja2.template('profile.html')
async def handle_profile(request):
    # Получаем tg_id из параметров запроса или из JWT токена
    token = request.query.get('token')
    if token:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            tg_id = payload.get('tg_id')
        except jwt.ExpiredSignatureError:
            return {'error': 'Сессия истекла. Пожалуйста, перезапустите бота.'}
        except jwt.InvalidTokenError:
            return {'error': 'Неверный токен. Пожалуйста, перезапустите бота.'}
    else:
        tg_id = request.query.get('tg_id')

    if not tg_id:
        return {'error': 'Необходима авторизация через Telegram.'}

    async with AsyncSessionLocal() as session:
        result = await session.execute(
            "SELECT * FROM users WHERE tg_id = :tg_id",
            {"tg_id": tg_id}
        )
        user = result.fetchone()
        if user:
            person_result = await session.execute(
                "SELECT * FROM persons WHERE id = :id",
                {"id": user.linked_person_id}
            )
            person = person_result.fetchone()
            if person:
                return {'person': person}
            else:
                return {'error': 'Личная карточка не найдена.'}
        else:
            return {'error': 'У вас нет доступа к информации.'}

def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app, loader=FileSystemLoader('webapp/templates')
    )
    app.router.add_get('/', handle_profile)
    return app

async def start_webapp():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, WEBAPP_HOST, WEBAPP_PORT)
    await site.start()
