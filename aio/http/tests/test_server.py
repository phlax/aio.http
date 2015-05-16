import os
import asyncio

import aiohttp

from aio.testing import aiotest, aiofuturetest
from aio.app.testing import AioAppTestCase
from aio.signals import Signals
import aio.app
from aio.app.runner import runner

HTTP_CONFIG = """
[aio:commands]
run: aio.app.cmd.cmd_run

[server:test]
factory: aio.http.server.http_server
root: aio.http.tests.test_server.test_root
address: 0.0.0.0
port: 7071
"""

@asyncio.coroutine
def test_root(webapp):

    @asyncio.coroutine
    def handle_hello_world(webapp):
        return aiohttp.web.Response(body=b"Hello, world")

    webapp.router.add_route("GET", "/", handle_hello_world)


class HttpServerTestCase(AioAppTestCase):
    
    @aiofuturetest(sleep=2)
    def test_http_server(self):
        yield from runner(
            ['run'], config_string=HTTP_CONFIG)

        @asyncio.coroutine
        def _test():
            response = yield from aiohttp.request(
                'GET', "http://localhost:7071")
            self.assertEqual(
                response.status, 200)
            body = yield from response.read()
            self.assertEqual(
                body, b"Hello, world")

        return _test
