import argparse
import asyncio


def create_handler(buff_size, log):
    async def handler(reader, writer):
        while True:
            try:
                chunk = await reader.read(buff_size)

                if not chunk:
                    writer.close()
                    log('Client connection closed')
                    await writer.wait_closed()
                    return

                log(f"Received: {chunk}")
                writer.write(chunk)

                # Uncomment if you need http response
                # Note: We don't close connection in such case so be sure that your clients sends keep-alive header
                # writer.write(f"HTTP/1.1 200 OK\r\nContent-Length:0\r\n\r\n".encode())

                await writer.drain()
            except ConnectionResetError:
                log('Client connection lost')
                return

    return handler


def create_logger(silent):
    def log(message):
        if not silent:
            print(message)

    return log


async def start_server(args):
    server = await asyncio.start_server(
        create_handler(args.buffer, create_logger(args.silent)),
        host=args.host,
        port=args.port,
        backlog=args.backlog
    )

    async with server:
        print(f'Serving on {args.host}:{args.port}...')
        await server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser(
        description='Asynchronous echo server',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument_group('required arguments') \
        .add_argument('--port', type=int, help='port to bind to')

    parser.add_argument('--host', type=str, help='host to bind to', default='localhost')
    parser.add_argument('--backlog', type=int, help='backlog for server socket', default=100)
    parser.add_argument('--buffer', type=int, help='read buffer size', default=8 * 1024)
    parser.add_argument('--silent', action='store_true', help='do not log anything during handling connections')

    return parser.parse_args()


def main():
    args = parse_args()
    try:
        asyncio.run(start_server(args))
    except KeyboardInterrupt:
        print('\nShutting down...')


if __name__ == '__main__':
    main()
