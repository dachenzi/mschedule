from aiohttp import web
import zerorpc


class Web:

    def __init__(self):
        self.app = web.Application()
        self.app.add_routes([
            web.get('/agent/list', self.agents_handle),
            web.post('/task', self.task_handler)
            # web.get('/echo', wshandle),
            # web.get('/{name}', handle)
        ])
        self.client = zerorpc.Client()
        # TODO 重连
        self.client.connect('tcp://127.0.0.1:9000')

    async def agents_handle(self, request: web.Request):
        ags = self.client.agents()
        return web.json_response(ags)
        # return web.Response(text='abcd1234')

    async def task_handler(self, request: web.Request):
        a = await request.json()
        task_id = self.client.add_task(a)
        return web.json_response(task_id)

    def start(self):
        web.run_app(self.app, host='0.0.0.0', port=8080)

    def shutdown(self):
        pass

# b35e71eb3ccb4d9aa9ed8cf3e14c52ff
