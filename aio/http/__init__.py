import asyncio

import aiohttp.web

import logging
log = logging.getLogger("aio.http")


@asyncio.coroutine
def protocol_factory(name):
    loop = asyncio.get_event_loop()
    http_app = aiohttp.web.Application(loop=loop)
    http_app['name'] = name
    return http_app.make_handler()


@asyncio.coroutine
def server(name, protocol, address, port):
    loop = asyncio.get_event_loop()

    if not protocol:
        protocol = protocol_factory

    protocol = yield from protocol(name)

    srv = yield from loop.create_server(
        protocol,
        address, port)
    log.info("Server(%s) started at http://%s:%s" % (name, address, port))
    return srv
