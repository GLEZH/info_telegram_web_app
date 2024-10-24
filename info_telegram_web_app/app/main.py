import asyncio
from app.bot import start_bot
from webapp.server import start_webapp

async def main():
    await asyncio.gather(
        start_bot(),
        start_webapp()
    )

if __name__ == '__main__':
    asyncio.run(main())
