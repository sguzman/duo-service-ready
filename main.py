import atexit
import concurrent
import concurrent.futures as futures
import grpc
import logging
import os
import typing
from typing import Dict

import server_pb2
import server_pb2_grpc


port: str = None
cache: Dict[str, str] = {}


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


def init_server() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    server_pb2_grpc.add_ConfServicer_to_server(Server(), server)
    server.add_insecure_port(f'localhost:{port}')

    server.start()
    logging.info('Started server at %s', port)
    server.wait_for_termination()

    logging.info('Ending server')


class Server(server_pb2_grpc.ConfServicer):
    def GetKey(self, request, context):
        key: str = request.key
        logging.info('Got request for key %s', key)
        value: str = cache.get(key)

        return server_pb2.ConfValue(value=value)

    def SetKey(self, request, context):
        key: str = request.key
        value: str = request.value
        logging.info('Set key "%s" to "%s"', key, value)

        cache[key] = value
        return server_pb2.Ack(ok=True)


def init() -> None:
    init_logging()
    init_atexit()
    init_env()
    init_server()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
