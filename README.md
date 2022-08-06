### Asynchronous TCP echo-server

Asynchronous TCP echo-server built on top of the python asyncio. Does not have any dependencies.

> Note: Use can use `ncat -e /bin/cat -k -l 8888` but if it's not available for you by some reason, or you want to add some more functionality (by modifying this source code) you can use this one.

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

Send something:
```
nc -v localhost 8888
hello
hello
```
