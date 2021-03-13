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


name: str = 'Ready Service'
port: str = None
cache: Dict[str, bool] = {}


def init_env() -> None:
    global port
    port = os.environ['PORT']

    logging.info('Found PORT at %s', port)


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
    server_pb2_grpc.add_ReadyServicer_to_server(Server(), server)
    server.add_insecure_port(f'localhost:{port}')

    server.start()
    logging.info('Started server at %s', port)
    server.wait_for_termination()

    logging.info('Ending server')


class Server(server_pb2_grpc.ReadyServicer):
    def RegisterService(self, request, context):
        service: str = request.name
        logging.info('Registering service %s', service)
        cache[service] = False

        return server_pb2.ReadyStatus(ready=False)

    def Ready(self, request, context):
        service: str = request.name
        if service in cache:
            logging.info('Getting status for "%s" = "%r"', key, value)
            value: bool = cache[service]
            return server_pb2.ReadyStatus(ready=value)
        else:
            logging.info('Service "%s" not found - setting to False', key)
            value: bool = False
            cache[service] = value

        return server_pb2.ReadyStatus(ready=value)


def init() -> None:
    init_logging()
    init_atexit()
    init_env()
    init_server()


def main() -> None:
    init()


if __name__ == '__main__':
    main()
