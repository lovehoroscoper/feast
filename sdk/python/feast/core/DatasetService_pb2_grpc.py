# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from feast.core import DatasetService_pb2 as feast_dot_core_dot_DatasetService__pb2


class DatasetServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateDataset = channel.unary_unary(
        '/feast.core.DatasetService/CreateDataset',
        request_serializer=feast_dot_core_dot_DatasetService__pb2.DatasetServiceTypes.CreateDatasetRequest.SerializeToString,
        response_deserializer=feast_dot_core_dot_DatasetService__pb2.DatasetServiceTypes.CreateDatasetResponse.FromString,
        )


class DatasetServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateDataset(self, request, context):
    """Create training dataset for a feature set
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatasetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateDataset': grpc.unary_unary_rpc_method_handler(
          servicer.CreateDataset,
          request_deserializer=feast_dot_core_dot_DatasetService__pb2.DatasetServiceTypes.CreateDatasetRequest.FromString,
          response_serializer=feast_dot_core_dot_DatasetService__pb2.DatasetServiceTypes.CreateDatasetResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'feast.core.DatasetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
