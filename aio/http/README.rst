aio.http usage
==============


Configuration
-------------

Create a config defining a factory method and a root handler

  >>> config = """
  ... [aio]
  ... log_level = ERROR
  ... 
  ... [server:test]
  ... factory: aio.http.server
  ... port: 7070
  ... """  


Running an http server
----------------------

By default the http server will respond with a 404 as there are no routes set up

  >>> import asyncio
  >>> import aiohttp
  >>> from aio.app.runner import runner  

  >>> def run_http_server():
  ...     yield from runner(['run'], config_string=config)
  ... 
  ...     @asyncio.coroutine
  ...     def _test_http_server():
  ...         result = yield from (
  ...             yield from aiohttp.request(
  ...                "GET", "http://localhost:7070")).read()  
  ...         print(result)
  ... 
  ...     return _test_http_server

  >>> from aio.testing import aiofuturetest
  >>> aiofuturetest(run_http_server, sleep=1)()  
  b'404: Not Found'

The server object is accessible from the aio.app.servers[{name}] var

  >>> import aio.app
  
  >>> aio.app.servers['test']
  <Server sockets=[<socket.socket...laddr=('0.0.0.0', 7070)...]>

Lets clear the app

  >>> aio.app.clear()
  

Running the server with a custom protocol
-----------------------------------------

If you specify a protocol in the server: config, the http server will use that function as a protocol factory.

The function should be a coroutine and is called with the name of the server

  >>> def http_protocol_factory(name):
  ...     loop = asyncio.get_event_loop()
  ...     webapp = aiohttp.web.Application(loop=loop)
  ...     webapp['name'] = name
  ... 
  ...     def handle_hello_world(webapp):
  ...         return aiohttp.web.Response(body=b"Hello, world")
  ... 
  ...     webapp.router.add_route("GET", "/", asyncio.coroutine(handle_hello_world))
  ...     return webapp.make_handler()

  >>> aio.http.tests._test_http_protocol = asyncio.coroutine(http_protocol_factory)
  
  >>> config_with_protocol = """
  ... [aio]
  ... log_level = ERROR
  ... 
  ... [server:test]
  ... factory: aio.http.server
  ... protocol: aio.http.tests._test_http_protocol
  ... port: 7070
  ... """  
  
  >>> def run_http_server():
  ...     yield from runner(['run'], config_string=config_with_protocol)
  ... 
  ...     @asyncio.coroutine
  ...     def _test_http_server():
  ...         result = yield from (
  ...             yield from aiohttp.request(
  ...                "GET", "http://localhost:7070")).read()
  ... 
  ...         print(result)
  ... 
  ...     return _test_http_server
  

  >>> aiofuturetest(run_http_server, sleep=1)()  
  b'Hello, world'

  >>> del aio.http.tests._test_http_protocol
  >>> aio.app.clear()
