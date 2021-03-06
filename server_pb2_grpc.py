# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class ReadyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterService = channel.unary_unary(
                '/Ready/RegisterService',
                request_serializer=server__pb2.ReadyService.SerializeToString,
                response_deserializer=server__pb2.ReadyStatus.FromString,
                )
        self.Ready = channel.unary_unary(
                '/Ready/Ready',
                request_serializer=server__pb2.ReadyService.SerializeToString,
                response_deserializer=server__pb2.ReadyStatus.FromString,
                )
        self.GetInventory = channel.unary_unary(
                '/Ready/GetInventory',
                request_serializer=server__pb2.ReadyStatus.SerializeToString,
                response_deserializer=server__pb2.ReadyList.FromString,
                )


class ReadyServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ready(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInventory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReadyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterService': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterService,
                    request_deserializer=server__pb2.ReadyService.FromString,
                    response_serializer=server__pb2.ReadyStatus.SerializeToString,
            ),
            'Ready': grpc.unary_unary_rpc_method_handler(
                    servicer.Ready,
                    request_deserializer=server__pb2.ReadyService.FromString,
                    response_serializer=server__pb2.ReadyStatus.SerializeToString,
            ),
            'GetInventory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInventory,
                    request_deserializer=server__pb2.ReadyStatus.FromString,
                    response_serializer=server__pb2.ReadyList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ready', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Ready(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ready/RegisterService',
            server__pb2.ReadyService.SerializeToString,
            server__pb2.ReadyStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Ready(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ready/Ready',
            server__pb2.ReadyService.SerializeToString,
            server__pb2.ReadyStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInventory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ready/GetInventory',
            server__pb2.ReadyStatus.SerializeToString,
            server__pb2.ReadyList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
