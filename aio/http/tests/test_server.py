import os
import asyncio

import aiohttp

from aio.testing import aiotest, aiofuturetest
from aio.app.testing import AioAppTestCase
from aio.signals import Signals
import aio.app
from aio.app.runner import runner

TEST_DIR = os.path.dirname(__file__)


@asyncio.coroutine
def handle_hello_world(app):
    return aiohttp.web.Response(body=b"Hello, world")


@asyncio.coroutine
def test_root(app):
    app.router.add_route("GET", "/", handle_hello_world)


HTTP_CONFIG = """
[aio:commands]
run: aio.app.cmd.cmd_run

[server:test]
factory: aio.http.server.http_server
root: aio.http.tests.test_server.test_root
address: 0.0.0.0
port: 7070
"""

class HttpServerTestCase(AioAppTestCase):

    @aiofuturetest(sleep=2)
    def test_http_server(self):
        yield from runner(
            ['run'], config_string=HTTP_CONFIG)

        @asyncio.coroutine
        def _test():
            response = yield from aiohttp.request(
                'GET', "http://localhost:7070")
            self.assertEquals(
                response.status, 200)
            body = yield from response.read()
            self.assertEquals(
                body, b"Hello, world")

        return _test
