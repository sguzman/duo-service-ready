import atexit
import grpc
import logging
import os

import server_pb2
import server_pb2_grpc


port: str = None


def init_env() -> None:
    global port
    port = os.environ['CONF_PORT']

    logging.info('Found CONF_PORT at %s', port)


def init_atexit() -> None:
    def end():
        logging.info('bye')

    atexit.register(end)


def init_logging() -> None:
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('hi')


def init_client() -> None:
    addr: str = f'localhost:{port}'
    logging.info('Calling %s', addr)

    channel = grpc.insecure_channel(addr)
    stub = server_pb2_grpc.ConfStub(channel)

    key: str = 'key'
    value: str = 'value'
    response = stub.SetKey(server_pb2.ConfKeyValue(key=key, value=value))
    ack: bool = response.ok

    logging.info('Set key "%s" to value "%s" and got resp %r', key, value, ack)

    response2 = stub.GetKey(server_pb2.ConfKey(key=key))
    logging.info('Queried key "%s" and got "%s"', key, value)


def init() -> None:
    init_logging()
    init_atexit()
    init_env()
    init_client()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
