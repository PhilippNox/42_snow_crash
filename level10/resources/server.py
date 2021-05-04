from aiohttp import web

async def handle(request):
    print(request, request.content_type, request.has_body, f"text: {await request.text()}")
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello, {name}\n"
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app, port=6969)
