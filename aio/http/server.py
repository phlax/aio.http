import asyncio

from zope.dottedname.resolve import resolve
import aiohttp

import aio.app

import logging
log = logging.getLogger("aio.http")


@asyncio.coroutine
def http_server(name, address, port):
    conf = aio.app.config["server:%s" % name]
    loop = asyncio.get_event_loop()
    app = aiohttp.web.Application(loop=loop)
    app['name'] = name
    yield from resolve(conf['root'])(app)
    srv = yield from loop.create_server(
        app.make_handler(),
        address, port)
    log.info("Server(%s) started at http://127.0.0.1:%s" % (name, port))
    return srv
