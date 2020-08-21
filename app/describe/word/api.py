from uuid import UUID, uuid4

from aiohttp import web
word_api = web.RouteTableDef()


@word_api.post(URL_WORDS)
async def post_word(request: web.Request) -> web.Response:
    data = await request.json()
    command = CreateWord()
    handler = await create_word_handler()
    async with orm.aquire() as connection:
        async with connection
