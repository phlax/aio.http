import asyncio

from zope.dottedname.resolve import resolve
import aiohttp.web

import aio.app

import logging
log = logging.getLogger("aio.http")


@asyncio.coroutine
def server(name, protocol, address, port):
    loop = asyncio.get_event_loop()

    if protocol:
        protocol = yield from protocol(name)
    else:
        app = aiohttp.web.Application(loop=loop)
        app['name'] = name
        protocol = app.make_handler()

    srv = yield from loop.create_server(
        protocol,
        address, port)
    log.info("Server(%s) started at http://%s:%s" % (name, address, port))
    return srv
