# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/packed_field_test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/packed_field_test.proto',
  package='google.protobuf.python.internal',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n0google/protobuf/internal/packed_field_test.proto\x12\x1fgoogle.protobuf.python.internal\"\xdb\x03\n\x0fTestPackedTypes\x12\x16\n\x0erepeated_int32\x18\x01 \x03(\x05\x12\x16\n\x0erepeated_int64\x18\x02 \x03(\x03\x12\x17\n\x0frepeated_uint32\x18\x03 \x03(\r\x12\x17\n\x0frepeated_uint64\x18\x04 \x03(\x04\x12\x17\n\x0frepeated_sint32\x18\x05 \x03(\x11\x12\x17\n\x0frepeated_sint64\x18\x06 \x03(\x12\x12\x18\n\x10repeated_fixed32\x18\x07 \x03(\x07\x12\x18\n\x10repeated_fixed64\x18\x08 \x03(\x06\x12\x19\n\x11repeated_sfixed32\x18\t \x03(\x0f\x12\x19\n\x11repeated_sfixed64\x18\n \x03(\x10\x12\x16\n\x0erepeated_float\x18\x0b \x03(\x02\x12\x17\n\x0frepeated_double\x18\x0c \x03(\x01\x12\x15\n\rrepeated_bool\x18\r \x03(\x08\x12Y\n\x14repeated_nested_enum\x18\x0e \x03(\x0e\x32;.google.protobuf.python.internal.TestPackedTypes.NestedEnum\"\'\n\nNestedEnum\x12\x07\n\x03\x46OO\x10\x00\x12\x07\n\x03\x42\x41R\x10\x01\x12\x07\n\x03\x42\x41Z\x10\x02\"\xec\x03\n\x11TestUnpackedTypes\x12\x1a\n\x0erepeated_int32\x18\x01 \x03(\x05\x42\x02\x10\x00\x12\x1a\n\x0erepeated_int64\x18\x02 \x03(\x03\x42\x02\x10\x00\x12\x1b\n\x0frepeated_uint32\x18\x03 \x03(\rB\x02\x10\x00\x12\x1b\n\x0frepeated_uint64\x18\x04 \x03(\x04\x42\x02\x10\x00\x12\x1b\n\x0frepeated_sint32\x18\x05 \x03(\x11\x42\x02\x10\x00\x12\x1b\n\x0frepeated_sint64\x18\x06 \x03(\x12\x42\x02\x10\x00\x12\x1c\n\x10repeated_fixed32\x18\x07 \x03(\x07\x42\x02\x10\x00\x12\x1c\n\x10repeated_fixed64\x18\x08 \x03(\x06\x42\x02\x10\x00\x12\x1d\n\x11repeated_sfixed32\x18\t \x03(\x0f\x42\x02\x10\x00\x12\x1d\n\x11repeated_sfixed64\x18\n \x03(\x10\x42\x02\x10\x00\x12\x1a\n\x0erepeated_float\x18\x0b \x03(\x02\x42\x02\x10\x00\x12\x1b\n\x0frepeated_double\x18\x0c \x03(\x01\x42\x02\x10\x00\x12\x19\n\rrepeated_bool\x18\r \x03(\x08\x42\x02\x10\x00\x12]\n\x14repeated_nested_enum\x18\x0e \x03(\x0e\x32;.google.protobuf.python.internal.TestPackedTypes.NestedEnumB\x02\x10\x00\x62\x06proto3'
)



_TESTPACKEDTYPES_NESTEDENUM = _descriptor.EnumDescriptor(
  name='NestedEnum',
  full_name='google.protobuf.python.internal.TestPackedTypes.NestedEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FOO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAZ', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=522,
  serialized_end=561,
)
_sym_db.RegisterEnumDescriptor(_TESTPACKEDTYPES_NESTEDENUM)


_TESTPACKEDTYPES = _descriptor.Descriptor(
  name='TestPackedTypes',
  full_name='google.protobuf.python.internal.TestPackedTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repeated_int32', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_int32', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_int64', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_int64', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_uint32', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_uint32', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_uint64', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_uint64', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sint32', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_sint32', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sint64', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_sint64', index=5,
      number=6, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_fixed32', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_fixed32', index=6,
      number=7, type=7, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_fixed64', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_fixed64', index=7,
      number=8, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sfixed32', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_sfixed32', index=8,
      number=9, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sfixed64', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_sfixed64', index=9,
      number=10, type=16, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_float', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_float', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_double', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_double', index=11,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_bool', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_bool', index=12,
      number=13, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_nested_enum', full_name='google.protobuf.python.internal.TestPackedTypes.repeated_nested_enum', index=13,
      number=14, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TESTPACKEDTYPES_NESTEDENUM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=561,
)


_TESTUNPACKEDTYPES = _descriptor.Descriptor(
  name='TestUnpackedTypes',
  full_name='google.protobuf.python.internal.TestUnpackedTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repeated_int32', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_int32', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_int64', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_int64', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_uint32', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_uint32', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_uint64', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_uint64', index=3,
      number=4, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sint32', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_sint32', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sint64', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_sint64', index=5,
      number=6, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_fixed32', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_fixed32', index=6,
      number=7, type=7, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_fixed64', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_fixed64', index=7,
      number=8, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sfixed32', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_sfixed32', index=8,
      number=9, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_sfixed64', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_sfixed64', index=9,
      number=10, type=16, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_float', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_float', index=10,
      number=11, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_double', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_double', index=11,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_bool', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_bool', index=12,
      number=13, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeated_nested_enum', full_name='google.protobuf.python.internal.TestUnpackedTypes.repeated_nested_enum', index=13,
      number=14, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\000', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=1056,
)

_TESTPACKEDTYPES.fields_by_name['repeated_nested_enum'].enum_type = _TESTPACKEDTYPES_NESTEDENUM
_TESTPACKEDTYPES_NESTEDENUM.containing_type = _TESTPACKEDTYPES
_TESTUNPACKEDTYPES.fields_by_name['repeated_nested_enum'].enum_type = _TESTPACKEDTYPES_NESTEDENUM
DESCRIPTOR.message_types_by_name['TestPackedTypes'] = _TESTPACKEDTYPES
DESCRIPTOR.message_types_by_name['TestUnpackedTypes'] = _TESTUNPACKEDTYPES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestPackedTypes = _reflection.GeneratedProtocolMessageType('TestPackedTypes', (_message.Message,), {
  'DESCRIPTOR' : _TESTPACKEDTYPES,
  '__module__' : 'google.protobuf.internal.packed_field_test_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.TestPackedTypes)
  })
_sym_db.RegisterMessage(TestPackedTypes)

TestUnpackedTypes = _reflection.GeneratedProtocolMessageType('TestUnpackedTypes', (_message.Message,), {
  'DESCRIPTOR' : _TESTUNPACKEDTYPES,
  '__module__' : 'google.protobuf.internal.packed_field_test_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.TestUnpackedTypes)
  })
_sym_db.RegisterMessage(TestUnpackedTypes)


_TESTUNPACKEDTYPES.fields_by_name['repeated_int32']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_int64']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_uint32']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_uint64']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_sint32']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_sint64']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_fixed32']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_fixed64']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_sfixed32']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_sfixed64']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_float']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_double']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_bool']._options = None
_TESTUNPACKEDTYPES.fields_by_name['repeated_nested_enum']._options = None
# @@protoc_insertion_point(module_scope)
