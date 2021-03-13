import atexit
import grpc
import logging
import os

import server_pb2
import server_pb2_grpc


port: str = None


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


def set_service(stub, service: str) -> server_pb2.ReadyStatus:
    response = stub.RegisterService(server_pb2.ReadyService(name=service))
    ack: bool = response.ready
    logging.info('Registered service "%s" - got response %r', service, ack)


def get_inv(stub) -> None:
    response = stub.GetInventory(server_pb2.ReadyStatus(ready=True))
    for s in response.entry:
        logging.info('Got service "%s" with status %r', s.name, s.ready)


def get_status(stub, service: str) -> None:
    response = stub.RegisterService(server_pb2.Ready(name=service))
    ack: bool = response.ready
    logging.info('Got service "%s" - got status %r', service, ack)


def init_client() -> None:
    addr: str = f'localhost:{port}'
    logging.info('Calling %s', addr)

    channel = grpc.insecure_channel(addr)
    stub = server_pb2_grpc.ReadyStub(channel)
    services: List[str] = ['A', 'B', 'C']
    for s in services:
        set_service(stub, s)

    get_inv(stub)

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
