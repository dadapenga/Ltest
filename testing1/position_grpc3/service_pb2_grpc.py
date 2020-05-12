# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class PositionProfileStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GenAxis1Profile = channel.unary_unary(
        '/positionProfile.PositionProfile/GenAxis1Profile',
        request_serializer=service__pb2.GenAxis1PositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.GenAxis1PositionProfileResponse.FromString,
        )
    self.FixAxis1Profile = channel.unary_unary(
        '/positionProfile.PositionProfile/FixAxis1Profile',
        request_serializer=service__pb2.FixAxis1PositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.FixAxis1PositionProfileResponse.FromString,
        )
    self.GenFullProfile = channel.unary_unary(
        '/positionProfile.PositionProfile/GenFullProfile',
        request_serializer=service__pb2.GenFullPositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.GenFullPositionProfileResponse.FromString,
        )
    self.GenProfile = channel.unary_unary(
        '/positionProfile.PositionProfile/GenProfile',
        request_serializer=service__pb2.GenPositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.GenPositionProfileResponse.FromString,
        )
    self.GenProfileChannel = channel.stream_stream(
        '/positionProfile.PositionProfile/GenProfileChannel',
        request_serializer=service__pb2.GenPositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.GenPositionProfileResponse.FromString,
        )
    self.GetProfile = channel.unary_unary(
        '/positionProfile.PositionProfile/GetProfile',
        request_serializer=service__pb2.GetPositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.GetPositionProfileResponse.FromString,
        )
    self.GetProfileChannel = channel.stream_stream(
        '/positionProfile.PositionProfile/GetProfileChannel',
        request_serializer=service__pb2.GetPositionProfileRequest.SerializeToString,
        response_deserializer=service__pb2.GetPositionProfileResponse.FromString,
        )


class PositionProfileServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GenAxis1Profile(self, request, context):
    """生成一级维度画像
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FixAxis1Profile(self, request, context):
    """修复一级维度画像
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenFullProfile(self, request, context):
    """产生二、三级维度画像
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenProfile(self, request, context):
    """一次性产生全量画像
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenProfileChannel(self, request_iterator, context):
    """一次性产生全量画像-多路复用
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProfile(self, request, context):
    """获取历史画像
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetProfileChannel(self, request_iterator, context):
    """获取历史画像-多路复用
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PositionProfileServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenAxis1Profile': grpc.unary_unary_rpc_method_handler(
          servicer.GenAxis1Profile,
          request_deserializer=service__pb2.GenAxis1PositionProfileRequest.FromString,
          response_serializer=service__pb2.GenAxis1PositionProfileResponse.SerializeToString,
      ),
      'FixAxis1Profile': grpc.unary_unary_rpc_method_handler(
          servicer.FixAxis1Profile,
          request_deserializer=service__pb2.FixAxis1PositionProfileRequest.FromString,
          response_serializer=service__pb2.FixAxis1PositionProfileResponse.SerializeToString,
      ),
      'GenFullProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GenFullProfile,
          request_deserializer=service__pb2.GenFullPositionProfileRequest.FromString,
          response_serializer=service__pb2.GenFullPositionProfileResponse.SerializeToString,
      ),
      'GenProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GenProfile,
          request_deserializer=service__pb2.GenPositionProfileRequest.FromString,
          response_serializer=service__pb2.GenPositionProfileResponse.SerializeToString,
      ),
      'GenProfileChannel': grpc.stream_stream_rpc_method_handler(
          servicer.GenProfileChannel,
          request_deserializer=service__pb2.GenPositionProfileRequest.FromString,
          response_serializer=service__pb2.GenPositionProfileResponse.SerializeToString,
      ),
      'GetProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GetProfile,
          request_deserializer=service__pb2.GetPositionProfileRequest.FromString,
          response_serializer=service__pb2.GetPositionProfileResponse.SerializeToString,
      ),
      'GetProfileChannel': grpc.stream_stream_rpc_method_handler(
          servicer.GetProfileChannel,
          request_deserializer=service__pb2.GetPositionProfileRequest.FromString,
          response_serializer=service__pb2.GetPositionProfileResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'positionProfile.PositionProfile', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))