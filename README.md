aio.http
=======

Http server for the [aio](https://github.com/phlax/aio) asyncio framework

Build status
------------
[![Build Status](https://travis-ci.org/phlax/aio.http.svg?branch=master)](https://travis-ci.org/phlax/aio.http)

Installation
------------

Install with:

```
  pip install aio.http
```

Configuration
-------------

Example configuration for a hello world server

```
[aio:commands]
run: aio.app.cmd.cmd_run

[server:test]
factory: aio.http.server.http_server
root: aio.http.tests.test_server.test_root
address: 0.0.0.0
port: 8080
```


Running
-------

Run with the aio command

```
   aio run
```

See [aio.app](http://github.com/phlax/aio.app) for more information on the "aio run" command


Usage
-----
For more detailed information about using aio.http please see [aio/http](aio/http).
