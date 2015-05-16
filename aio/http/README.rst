========
aio.http
========


Installation
------------

Install with:

  pip install aio.http

Configuration
-------------

Create a config defining a factory method and a root handler

  >>> CONFIG = """
  ... [aio:commands]
  ... run: aio.app.cmd.cmd_run
  ... 
  ... [server:test]
  ... factory: aio.http.server.http_server
  ... root: aio.http.tests.test_server.test_root
  ... address: 0.0.0.0
  ... port: 7070
  ... """  

Running
-------

Run with the aio command

  # aio run


See http://github.com/phlax/aio.app for more information on the "aio run" command
  
Running the app
---------------

And define an object to collect the results

  >>> class Response:
  ...     body = None
  >>> response = Response()

Lets run an async test to get the default http response

  >>> import asyncio
  >>> import aiohttp
  >>> from aio.app.runner import runner  

  >>> def run_future_app():
  ...     yield from runner(['run'], config_string=CONFIG)
  ... 
  ...     @asyncio.coroutine
  ...     def _test_http():
  ...         response.body = yield from (
  ...             yield from aiohttp.request(
  ...                "GET", "http://localhost:7070")).read()
  ... 
  ...     return _test_http

And run the test

  >>> from aio.testing import aiofuturetest
  >>> aiofuturetest(run_future_app, timeout=5, sleep=2)()  

  >>> response.body
  b'Hello, world'

The server object is accessible from the aio.app.servers[{name}] var

  >>> import aio.app
  >>> aio.app.servers['test']
  <Server sockets=[<socket.socket ... laddr=('0.0.0.0', 7070)>]>

  >>> aio.app.clear()
