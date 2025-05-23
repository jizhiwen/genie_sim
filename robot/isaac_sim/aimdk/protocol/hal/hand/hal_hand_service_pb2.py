# -*- coding: utf-8 -*-
# Copyright (c) 2023-2025, AgiBot Inc. All Rights Reserved.
# Author: Genie Sim Team
# License: Mozilla Public License Version 2.0

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aimdk/protocol/hal/hand/hal_hand_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'aimdk/protocol/hal/hand/hal_hand_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aimdk.protocol.common import rpc_pb2 as aimdk_dot_protocol_dot_common_dot_rpc__pb2
try:
  aimdk_dot_protocol_dot_common_dot_timestamp__pb2 = aimdk_dot_protocol_dot_common_dot_rpc__pb2.aimdk_dot_protocol_dot_common_dot_timestamp__pb2
except AttributeError:
  aimdk_dot_protocol_dot_common_dot_timestamp__pb2 = aimdk_dot_protocol_dot_common_dot_rpc__pb2.aimdk.protocol.common.timestamp_pb2
try:
  aimdk_dot_protocol_dot_common_dot_header__pb2 = aimdk_dot_protocol_dot_common_dot_rpc__pb2.aimdk_dot_protocol_dot_common_dot_header__pb2
except AttributeError:
  aimdk_dot_protocol_dot_common_dot_header__pb2 = aimdk_dot_protocol_dot_common_dot_rpc__pb2.aimdk.protocol.common.header_pb2
from aimdk.protocol.common import header_pb2 as aimdk_dot_protocol_dot_common_dot_header__pb2
from aimdk.protocol.hal.hand import hand_pb2 as aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2
try:
  aimdk_dot_protocol_dot_common_dot_header__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk_dot_protocol_dot_common_dot_header__pb2
except AttributeError:
  aimdk_dot_protocol_dot_common_dot_header__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk.protocol.common.header_pb2
try:
  aimdk_dot_protocol_dot_hal_dot_hand_dot_inspire__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk_dot_protocol_dot_hal_dot_hand_dot_inspire__pb2
except AttributeError:
  aimdk_dot_protocol_dot_hal_dot_hand_dot_inspire__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk.protocol.hal.hand.inspire_pb2
try:
  aimdk_dot_protocol_dot_hal_dot_hand_dot_jodell__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk_dot_protocol_dot_hal_dot_hand_dot_jodell__pb2
except AttributeError:
  aimdk_dot_protocol_dot_hal_dot_hand_dot_jodell__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk.protocol.hal.hand.jodell_pb2
try:
  aimdk_dot_protocol_dot_hal_dot_hand_dot_agi__claw__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk_dot_protocol_dot_hal_dot_hand_dot_agi__claw__pb2
except AttributeError:
  aimdk_dot_protocol_dot_hal_dot_hand_dot_agi__claw__pb2 = aimdk_dot_protocol_dot_hal_dot_hand_dot_hand__pb2.aimdk.protocol.hal.hand.agi_claw_pb2

from aimdk.protocol.common.rpc_pb2 import *
from aimdk.protocol.common.header_pb2 import *
from aimdk.protocol.hal.hand.hand_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.aimdk/protocol/hal/hand/hal_hand_service.proto\x12\x0e\x61imdk.protocol\x1a\x1f\x61imdk/protocol/common/rpc.proto\x1a\"aimdk/protocol/common/header.proto\x1a\"aimdk/protocol/hal/hand/hand.proto\"l\n\x11HandStateResponse\x12.\n\x06header\x18\x01 \x01(\x0b\x32\x1e.aimdk.protocol.ResponseHeader\x12\'\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x19.aimdk.protocol.HandState\"n\n\x12HandCommandRequest\x12-\n\x06header\x18\x01 \x01(\x0b\x32\x1d.aimdk.protocol.RequestHeader\x12)\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1b.aimdk.protocol.HandCommand2\xb8\x01\n\x0eHalHandService\x12P\n\x0cGetHandState\x12\x1d.aimdk.protocol.CommonRequest\x1a!.aimdk.protocol.HandStateResponse\x12T\n\x0eSetHandCommand\x12\".aimdk.protocol.HandCommandRequest\x1a\x1e.aimdk.protocol.CommonResponseP\x00P\x01P\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aimdk.protocol.hal.hand.hal_hand_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HANDSTATERESPONSE']._serialized_start=171
  _globals['_HANDSTATERESPONSE']._serialized_end=279
  _globals['_HANDCOMMANDREQUEST']._serialized_start=281
  _globals['_HANDCOMMANDREQUEST']._serialized_end=391
  _globals['_HALHANDSERVICE']._serialized_start=394
  _globals['_HALHANDSERVICE']._serialized_end=578
# @@protoc_insertion_point(module_scope)
