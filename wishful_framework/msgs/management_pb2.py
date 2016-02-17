# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: management.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='management.proto',
  package='wishful_controller.framework',
  serialized_pb=_b('\n\x10management.proto\x12\x1cwishful_controller.framework\"\xbe\x03\n\x07\x43mdDesc\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x11\n\tfunc_name\x18\x02 \x02(\t\x12\x11\n\texec_time\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61ll_id\x18\x04 \x01(\t\x12\x11\n\tcaller_id\x18\x05 \x01(\t\x12\x16\n\x0etransaction_id\x18\x06 \x01(\t\x12U\n\x12serialization_type\x18\x07 \x01(\x0e\x32\x33.wishful_controller.framework.CmdDesc.Serialization:\x04NONE\x12\x17\n\x0frepeat_interval\x18\x08 \x01(\t\x12\x15\n\rrepeat_number\x18\t \x01(\r\x12Q\n\x11repeat_conditions\x18\n \x01(\x0b\x32\x36.wishful_controller.framework.CmdDesc.RepeatConditions\x1a\x34\n\x10RepeatConditions\x12\x11\n\tcondition\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r\"3\n\rSerialization\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06PICKLE\x10\x01\x12\x0c\n\x08PROTOBUF\x10\x02\"\xe9\x03\n\x08RuleDesc\x12;\n\x05match\x18\x01 \x02(\x0b\x32,.wishful_controller.framework.RuleDesc.Match\x12=\n\x06\x61\x63tion\x18\x02 \x02(\x0b\x32-.wishful_controller.framework.RuleDesc.Action\x12P\n\npermanence\x18\x03 \x02(\x0e\x32\x31.wishful_controller.framework.RuleDesc.Permanence:\tTRANSIENT\x12\x10\n\x08\x63\x61llback\x18\x04 \x02(\t\x1a\x97\x01\n\x05Match\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x11\n\tfunc_name\x18\x02 \x02(\t\x12\x13\n\x0b\x66ilter_type\x18\x03 \x02(\t\x12\x1a\n\x12\x66ilter_window_type\x18\x04 \x02(\t\x12\x1a\n\x12\x66ilter_window_size\x18\x05 \x02(\t\x12\x11\n\tcondition\x18\x06 \x02(\t\x12\r\n\x05value\x18\x07 \x02(\t\x1a\x37\n\x06\x41\x63tion\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\x11\n\tfunc_name\x18\x02 \x02(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x02(\t\"*\n\nPermanence\x12\r\n\tTRANSIENT\x10\x00\x12\r\n\tPERMANENT\x10\x01\"e\n\x07MsgDesc\x12\x10\n\x08msg_type\x18\x01 \x02(\t\x12\x11\n\texec_time\x18\x02 \x01(\t\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x0c\n\x04uuid\x18\x04 \x01(\t\x12\x0f\n\x07msg_set\x18\x05 \x01(\x08\"\xbf\x01\n\nNewNodeMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x0f\n\x07modules\x18\x04 \x03(\t\x12\x46\n\nattributes\x18\x05 \x03(\x0b\x32\x32.wishful_controller.framework.NewNodeMsg.Attribute\x1a(\n\tAttribute\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"Y\n\nNewNodeAck\x12\x0e\n\x06status\x18\x01 \x02(\x08\x12\x17\n\x0f\x63ontroller_uuid\x18\x02 \x01(\t\x12\x12\n\nagent_uuid\x18\x03 \x01(\t\x12\x0e\n\x06topics\x18\x04 \x03(\t\"1\n\x0bNodeExitMsg\x12\x12\n\nagent_uuid\x18\x01 \x02(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"K\n\x17\x43ontrollerDiscoveredMsg\x12\x11\n\tdown_link\x18\x01 \x01(\t\x12\x0f\n\x07up_link\x18\x02 \x01(\t\x12\x0c\n\x04pair\x18\x03 \x01(\t\"%\n\x13\x44iscoverySuccessMsg\x12\x0e\n\x06status\x18\x01 \x02(\x08\"%\n\x13\x44iscoveryRestartMsg\x12\x0e\n\x06reason\x18\x01 \x01(\t\")\n\x08HelloMsg\x12\x0c\n\x04uuid\x18\x01 \x02(\t\x12\x0f\n\x07timeout\x18\x02 \x02(\r\"!\n\x10\x45xampleModuleReq\x12\r\n\x05hello\x18\x01 \x01(\t\"!\n\x10\x45xampleModuleAck\x12\r\n\x05hello\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CMDDESC_SERIALIZATION = _descriptor.EnumDescriptor(
  name='Serialization',
  full_name='wishful_controller.framework.CmdDesc.Serialization',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PICKLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=446,
  serialized_end=497,
)
_sym_db.RegisterEnumDescriptor(_CMDDESC_SERIALIZATION)

_RULEDESC_PERMANENCE = _descriptor.EnumDescriptor(
  name='Permanence',
  full_name='wishful_controller.framework.RuleDesc.Permanence',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRANSIENT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERMANENT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=947,
  serialized_end=989,
)
_sym_db.RegisterEnumDescriptor(_RULEDESC_PERMANENCE)


_CMDDESC_REPEATCONDITIONS = _descriptor.Descriptor(
  name='RepeatConditions',
  full_name='wishful_controller.framework.CmdDesc.RepeatConditions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition', full_name='wishful_controller.framework.CmdDesc.RepeatConditions.condition', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='wishful_controller.framework.CmdDesc.RepeatConditions.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=392,
  serialized_end=444,
)

_CMDDESC = _descriptor.Descriptor(
  name='CmdDesc',
  full_name='wishful_controller.framework.CmdDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_controller.framework.CmdDesc.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_name', full_name='wishful_controller.framework.CmdDesc.func_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exec_time', full_name='wishful_controller.framework.CmdDesc.exec_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_id', full_name='wishful_controller.framework.CmdDesc.call_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caller_id', full_name='wishful_controller.framework.CmdDesc.caller_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='wishful_controller.framework.CmdDesc.transaction_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serialization_type', full_name='wishful_controller.framework.CmdDesc.serialization_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat_interval', full_name='wishful_controller.framework.CmdDesc.repeat_interval', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat_number', full_name='wishful_controller.framework.CmdDesc.repeat_number', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeat_conditions', full_name='wishful_controller.framework.CmdDesc.repeat_conditions', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CMDDESC_REPEATCONDITIONS, ],
  enum_types=[
    _CMDDESC_SERIALIZATION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=497,
)


_RULEDESC_MATCH = _descriptor.Descriptor(
  name='Match',
  full_name='wishful_controller.framework.RuleDesc.Match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_controller.framework.RuleDesc.Match.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_name', full_name='wishful_controller.framework.RuleDesc.Match.func_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_type', full_name='wishful_controller.framework.RuleDesc.Match.filter_type', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_window_type', full_name='wishful_controller.framework.RuleDesc.Match.filter_window_type', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_window_size', full_name='wishful_controller.framework.RuleDesc.Match.filter_window_size', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition', full_name='wishful_controller.framework.RuleDesc.Match.condition', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='wishful_controller.framework.RuleDesc.Match.value', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=888,
)

_RULEDESC_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='wishful_controller.framework.RuleDesc.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wishful_controller.framework.RuleDesc.Action.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='func_name', full_name='wishful_controller.framework.RuleDesc.Action.func_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='wishful_controller.framework.RuleDesc.Action.args', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=890,
  serialized_end=945,
)

_RULEDESC = _descriptor.Descriptor(
  name='RuleDesc',
  full_name='wishful_controller.framework.RuleDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='match', full_name='wishful_controller.framework.RuleDesc.match', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='action', full_name='wishful_controller.framework.RuleDesc.action', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='permanence', full_name='wishful_controller.framework.RuleDesc.permanence', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callback', full_name='wishful_controller.framework.RuleDesc.callback', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RULEDESC_MATCH, _RULEDESC_ACTION, ],
  enum_types=[
    _RULEDESC_PERMANENCE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=500,
  serialized_end=989,
)


_MSGDESC = _descriptor.Descriptor(
  name='MsgDesc',
  full_name='wishful_controller.framework.MsgDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_type', full_name='wishful_controller.framework.MsgDesc.msg_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exec_time', full_name='wishful_controller.framework.MsgDesc.exec_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='wishful_controller.framework.MsgDesc.transaction_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='wishful_controller.framework.MsgDesc.uuid', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_set', full_name='wishful_controller.framework.MsgDesc.msg_set', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=991,
  serialized_end=1092,
)


_NEWNODEMSG_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='wishful_controller.framework.NewNodeMsg.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.NewNodeMsg.Attribute.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='wishful_controller.framework.NewNodeMsg.Attribute.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1246,
  serialized_end=1286,
)

_NEWNODEMSG = _descriptor.Descriptor(
  name='NewNodeMsg',
  full_name='wishful_controller.framework.NewNodeMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NewNodeMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='wishful_controller.framework.NewNodeMsg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='wishful_controller.framework.NewNodeMsg.info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modules', full_name='wishful_controller.framework.NewNodeMsg.modules', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='wishful_controller.framework.NewNodeMsg.attributes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NEWNODEMSG_ATTRIBUTE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1095,
  serialized_end=1286,
)


_NEWNODEACK = _descriptor.Descriptor(
  name='NewNodeAck',
  full_name='wishful_controller.framework.NewNodeAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wishful_controller.framework.NewNodeAck.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='controller_uuid', full_name='wishful_controller.framework.NewNodeAck.controller_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NewNodeAck.agent_uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='topics', full_name='wishful_controller.framework.NewNodeAck.topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1377,
)


_NODEEXITMSG = _descriptor.Descriptor(
  name='NodeExitMsg',
  full_name='wishful_controller.framework.NodeExitMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uuid', full_name='wishful_controller.framework.NodeExitMsg.agent_uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='wishful_controller.framework.NodeExitMsg.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1379,
  serialized_end=1428,
)


_CONTROLLERDISCOVEREDMSG = _descriptor.Descriptor(
  name='ControllerDiscoveredMsg',
  full_name='wishful_controller.framework.ControllerDiscoveredMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='down_link', full_name='wishful_controller.framework.ControllerDiscoveredMsg.down_link', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='up_link', full_name='wishful_controller.framework.ControllerDiscoveredMsg.up_link', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pair', full_name='wishful_controller.framework.ControllerDiscoveredMsg.pair', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1430,
  serialized_end=1505,
)


_DISCOVERYSUCCESSMSG = _descriptor.Descriptor(
  name='DiscoverySuccessMsg',
  full_name='wishful_controller.framework.DiscoverySuccessMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wishful_controller.framework.DiscoverySuccessMsg.status', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1507,
  serialized_end=1544,
)


_DISCOVERYRESTARTMSG = _descriptor.Descriptor(
  name='DiscoveryRestartMsg',
  full_name='wishful_controller.framework.DiscoveryRestartMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='wishful_controller.framework.DiscoveryRestartMsg.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1546,
  serialized_end=1583,
)


_HELLOMSG = _descriptor.Descriptor(
  name='HelloMsg',
  full_name='wishful_controller.framework.HelloMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='wishful_controller.framework.HelloMsg.uuid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='wishful_controller.framework.HelloMsg.timeout', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1585,
  serialized_end=1626,
)


_EXAMPLEMODULEREQ = _descriptor.Descriptor(
  name='ExampleModuleReq',
  full_name='wishful_controller.framework.ExampleModuleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello', full_name='wishful_controller.framework.ExampleModuleReq.hello', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1628,
  serialized_end=1661,
)


_EXAMPLEMODULEACK = _descriptor.Descriptor(
  name='ExampleModuleAck',
  full_name='wishful_controller.framework.ExampleModuleAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hello', full_name='wishful_controller.framework.ExampleModuleAck.hello', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1663,
  serialized_end=1696,
)

_CMDDESC_REPEATCONDITIONS.containing_type = _CMDDESC
_CMDDESC.fields_by_name['serialization_type'].enum_type = _CMDDESC_SERIALIZATION
_CMDDESC.fields_by_name['repeat_conditions'].message_type = _CMDDESC_REPEATCONDITIONS
_CMDDESC_SERIALIZATION.containing_type = _CMDDESC
_RULEDESC_MATCH.containing_type = _RULEDESC
_RULEDESC_ACTION.containing_type = _RULEDESC
_RULEDESC.fields_by_name['match'].message_type = _RULEDESC_MATCH
_RULEDESC.fields_by_name['action'].message_type = _RULEDESC_ACTION
_RULEDESC.fields_by_name['permanence'].enum_type = _RULEDESC_PERMANENCE
_RULEDESC_PERMANENCE.containing_type = _RULEDESC
_NEWNODEMSG_ATTRIBUTE.containing_type = _NEWNODEMSG
_NEWNODEMSG.fields_by_name['attributes'].message_type = _NEWNODEMSG_ATTRIBUTE
DESCRIPTOR.message_types_by_name['CmdDesc'] = _CMDDESC
DESCRIPTOR.message_types_by_name['RuleDesc'] = _RULEDESC
DESCRIPTOR.message_types_by_name['MsgDesc'] = _MSGDESC
DESCRIPTOR.message_types_by_name['NewNodeMsg'] = _NEWNODEMSG
DESCRIPTOR.message_types_by_name['NewNodeAck'] = _NEWNODEACK
DESCRIPTOR.message_types_by_name['NodeExitMsg'] = _NODEEXITMSG
DESCRIPTOR.message_types_by_name['ControllerDiscoveredMsg'] = _CONTROLLERDISCOVEREDMSG
DESCRIPTOR.message_types_by_name['DiscoverySuccessMsg'] = _DISCOVERYSUCCESSMSG
DESCRIPTOR.message_types_by_name['DiscoveryRestartMsg'] = _DISCOVERYRESTARTMSG
DESCRIPTOR.message_types_by_name['HelloMsg'] = _HELLOMSG
DESCRIPTOR.message_types_by_name['ExampleModuleReq'] = _EXAMPLEMODULEREQ
DESCRIPTOR.message_types_by_name['ExampleModuleAck'] = _EXAMPLEMODULEACK

CmdDesc = _reflection.GeneratedProtocolMessageType('CmdDesc', (_message.Message,), dict(

  RepeatConditions = _reflection.GeneratedProtocolMessageType('RepeatConditions', (_message.Message,), dict(
    DESCRIPTOR = _CMDDESC_REPEATCONDITIONS,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.CmdDesc.RepeatConditions)
    ))
  ,
  DESCRIPTOR = _CMDDESC,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.CmdDesc)
  ))
_sym_db.RegisterMessage(CmdDesc)
_sym_db.RegisterMessage(CmdDesc.RepeatConditions)

RuleDesc = _reflection.GeneratedProtocolMessageType('RuleDesc', (_message.Message,), dict(

  Match = _reflection.GeneratedProtocolMessageType('Match', (_message.Message,), dict(
    DESCRIPTOR = _RULEDESC_MATCH,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc.Match)
    ))
  ,

  Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
    DESCRIPTOR = _RULEDESC_ACTION,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc.Action)
    ))
  ,
  DESCRIPTOR = _RULEDESC,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.RuleDesc)
  ))
_sym_db.RegisterMessage(RuleDesc)
_sym_db.RegisterMessage(RuleDesc.Match)
_sym_db.RegisterMessage(RuleDesc.Action)

MsgDesc = _reflection.GeneratedProtocolMessageType('MsgDesc', (_message.Message,), dict(
  DESCRIPTOR = _MSGDESC,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.MsgDesc)
  ))
_sym_db.RegisterMessage(MsgDesc)

NewNodeMsg = _reflection.GeneratedProtocolMessageType('NewNodeMsg', (_message.Message,), dict(

  Attribute = _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), dict(
    DESCRIPTOR = _NEWNODEMSG_ATTRIBUTE,
    __module__ = 'management_pb2'
    # @@protoc_insertion_point(class_scope:wishful_controller.framework.NewNodeMsg.Attribute)
    ))
  ,
  DESCRIPTOR = _NEWNODEMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NewNodeMsg)
  ))
_sym_db.RegisterMessage(NewNodeMsg)
_sym_db.RegisterMessage(NewNodeMsg.Attribute)

NewNodeAck = _reflection.GeneratedProtocolMessageType('NewNodeAck', (_message.Message,), dict(
  DESCRIPTOR = _NEWNODEACK,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NewNodeAck)
  ))
_sym_db.RegisterMessage(NewNodeAck)

NodeExitMsg = _reflection.GeneratedProtocolMessageType('NodeExitMsg', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXITMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.NodeExitMsg)
  ))
_sym_db.RegisterMessage(NodeExitMsg)

ControllerDiscoveredMsg = _reflection.GeneratedProtocolMessageType('ControllerDiscoveredMsg', (_message.Message,), dict(
  DESCRIPTOR = _CONTROLLERDISCOVEREDMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.ControllerDiscoveredMsg)
  ))
_sym_db.RegisterMessage(ControllerDiscoveredMsg)

DiscoverySuccessMsg = _reflection.GeneratedProtocolMessageType('DiscoverySuccessMsg', (_message.Message,), dict(
  DESCRIPTOR = _DISCOVERYSUCCESSMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.DiscoverySuccessMsg)
  ))
_sym_db.RegisterMessage(DiscoverySuccessMsg)

DiscoveryRestartMsg = _reflection.GeneratedProtocolMessageType('DiscoveryRestartMsg', (_message.Message,), dict(
  DESCRIPTOR = _DISCOVERYRESTARTMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.DiscoveryRestartMsg)
  ))
_sym_db.RegisterMessage(DiscoveryRestartMsg)

HelloMsg = _reflection.GeneratedProtocolMessageType('HelloMsg', (_message.Message,), dict(
  DESCRIPTOR = _HELLOMSG,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.HelloMsg)
  ))
_sym_db.RegisterMessage(HelloMsg)

ExampleModuleReq = _reflection.GeneratedProtocolMessageType('ExampleModuleReq', (_message.Message,), dict(
  DESCRIPTOR = _EXAMPLEMODULEREQ,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.ExampleModuleReq)
  ))
_sym_db.RegisterMessage(ExampleModuleReq)

ExampleModuleAck = _reflection.GeneratedProtocolMessageType('ExampleModuleAck', (_message.Message,), dict(
  DESCRIPTOR = _EXAMPLEMODULEACK,
  __module__ = 'management_pb2'
  # @@protoc_insertion_point(class_scope:wishful_controller.framework.ExampleModuleAck)
  ))
_sym_db.RegisterMessage(ExampleModuleAck)


# @@protoc_insertion_point(module_scope)
