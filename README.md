### Asynchronous TCP echo-server

Asynchronous TCP echo-server built on top of the python asyncio.

#### Usage

Download:
```
curl -O https://raw.githubusercontent.com/opennikish/py-tcp-echo-server/main/echo-server.py
```

Run:
```
python echo-server.py --port 8888
```

Options:
```
required arguments:
  --port PORT        port to bind to
  
optional arguments:
  -h, --help         show this help message and exit
  --host HOST        host to bind to (default: None)
  --backlog BACKLOG  backlog for server socket (default: 100)
  --buffer BUFFER    read buffer size (default: 8192)
  --silent           do not log anything during handling connections (default: False)
```
