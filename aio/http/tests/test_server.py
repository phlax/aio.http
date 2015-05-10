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


class HttpServerTestCase(AioAppTestCase):

    @aiofuturetest
    def test_http_server(self):
        yield from runner(
            ['run'],
            configfile=os.path.join(
                TEST_DIR,
                "resources", "test-1.conf"))

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
