# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='session.proto',
  package='session_manager',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rsession.proto\x12\x0fsession_manager\"F\n\x0bSignupInput\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\t\"4\n\x0cSignupOutput\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\"E\n\nLoginInput\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x03 \x01(\t\"3\n\x0bLoginOutput\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\"\"\n\x0bLogoutInput\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\"\x1e\n\x0cLogoutOutput\x12\x0e\n\x06status\x18\x01 \x01(\x05\" \n\rClassifyInput\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\x0c\"\x1f\n\x0e\x43lassifyOutput\x12\r\n\x05token\x18\x01 \x01(\x05\x32\xb7\x02\n\x0eSessionManager\x12G\n\x06SignUP\x12\x1c.session_manager.SignupInput\x1a\x1d.session_manager.SignupOutput\"\x00\x12\x44\n\x05Login\x12\x1b.session_manager.LoginInput\x1a\x1c.session_manager.LoginOutput\"\x00\x12G\n\x06Logout\x12\x1c.session_manager.LogoutInput\x1a\x1d.session_manager.LogoutOutput\"\x00\x12M\n\x08\x43lassify\x12\x1e.session_manager.ClassifyInput\x1a\x1f.session_manager.ClassifyOutput\"\x00\x62\x06proto3')
)




_SIGNUPINPUT = _descriptor.Descriptor(
  name='SignupInput',
  full_name='session_manager.SignupInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='session_manager.SignupInput.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='session_manager.SignupInput.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='session_manager.SignupInput.device_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=34,
  serialized_end=104,
)


_SIGNUPOUTPUT = _descriptor.Descriptor(
  name='SignupOutput',
  full_name='session_manager.SignupOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='session_manager.SignupOutput.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='session_manager.SignupOutput.access_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=106,
  serialized_end=158,
)


_LOGININPUT = _descriptor.Descriptor(
  name='LoginInput',
  full_name='session_manager.LoginInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='session_manager.LoginInput.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='session_manager.LoginInput.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_name', full_name='session_manager.LoginInput.device_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=160,
  serialized_end=229,
)


_LOGINOUTPUT = _descriptor.Descriptor(
  name='LoginOutput',
  full_name='session_manager.LoginOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='session_manager.LoginOutput.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='session_manager.LoginOutput.access_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=231,
  serialized_end=282,
)


_LOGOUTINPUT = _descriptor.Descriptor(
  name='LogoutInput',
  full_name='session_manager.LogoutInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_name', full_name='session_manager.LogoutInput.device_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=284,
  serialized_end=318,
)


_LOGOUTOUTPUT = _descriptor.Descriptor(
  name='LogoutOutput',
  full_name='session_manager.LogoutOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='session_manager.LogoutOutput.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=320,
  serialized_end=350,
)


_CLASSIFYINPUT = _descriptor.Descriptor(
  name='ClassifyInput',
  full_name='session_manager.ClassifyInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='session_manager.ClassifyInput.Content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=352,
  serialized_end=384,
)


_CLASSIFYOUTPUT = _descriptor.Descriptor(
  name='ClassifyOutput',
  full_name='session_manager.ClassifyOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='session_manager.ClassifyOutput.token', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=386,
  serialized_end=417,
)

DESCRIPTOR.message_types_by_name['SignupInput'] = _SIGNUPINPUT
DESCRIPTOR.message_types_by_name['SignupOutput'] = _SIGNUPOUTPUT
DESCRIPTOR.message_types_by_name['LoginInput'] = _LOGININPUT
DESCRIPTOR.message_types_by_name['LoginOutput'] = _LOGINOUTPUT
DESCRIPTOR.message_types_by_name['LogoutInput'] = _LOGOUTINPUT
DESCRIPTOR.message_types_by_name['LogoutOutput'] = _LOGOUTOUTPUT
DESCRIPTOR.message_types_by_name['ClassifyInput'] = _CLASSIFYINPUT
DESCRIPTOR.message_types_by_name['ClassifyOutput'] = _CLASSIFYOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignupInput = _reflection.GeneratedProtocolMessageType('SignupInput', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPINPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.SignupInput)
  })
_sym_db.RegisterMessage(SignupInput)

SignupOutput = _reflection.GeneratedProtocolMessageType('SignupOutput', (_message.Message,), {
  'DESCRIPTOR' : _SIGNUPOUTPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.SignupOutput)
  })
_sym_db.RegisterMessage(SignupOutput)

LoginInput = _reflection.GeneratedProtocolMessageType('LoginInput', (_message.Message,), {
  'DESCRIPTOR' : _LOGININPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.LoginInput)
  })
_sym_db.RegisterMessage(LoginInput)

LoginOutput = _reflection.GeneratedProtocolMessageType('LoginOutput', (_message.Message,), {
  'DESCRIPTOR' : _LOGINOUTPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.LoginOutput)
  })
_sym_db.RegisterMessage(LoginOutput)

LogoutInput = _reflection.GeneratedProtocolMessageType('LogoutInput', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTINPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.LogoutInput)
  })
_sym_db.RegisterMessage(LogoutInput)

LogoutOutput = _reflection.GeneratedProtocolMessageType('LogoutOutput', (_message.Message,), {
  'DESCRIPTOR' : _LOGOUTOUTPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.LogoutOutput)
  })
_sym_db.RegisterMessage(LogoutOutput)

ClassifyInput = _reflection.GeneratedProtocolMessageType('ClassifyInput', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYINPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.ClassifyInput)
  })
_sym_db.RegisterMessage(ClassifyInput)

ClassifyOutput = _reflection.GeneratedProtocolMessageType('ClassifyOutput', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYOUTPUT,
  '__module__' : 'session_pb2'
  # @@protoc_insertion_point(class_scope:session_manager.ClassifyOutput)
  })
_sym_db.RegisterMessage(ClassifyOutput)



_SESSIONMANAGER = _descriptor.ServiceDescriptor(
  name='SessionManager',
  full_name='session_manager.SessionManager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=420,
  serialized_end=731,
  methods=[
  _descriptor.MethodDescriptor(
    name='SignUP',
    full_name='session_manager.SessionManager.SignUP',
    index=0,
    containing_service=None,
    input_type=_SIGNUPINPUT,
    output_type=_SIGNUPOUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='session_manager.SessionManager.Login',
    index=1,
    containing_service=None,
    input_type=_LOGININPUT,
    output_type=_LOGINOUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Logout',
    full_name='session_manager.SessionManager.Logout',
    index=2,
    containing_service=None,
    input_type=_LOGOUTINPUT,
    output_type=_LOGOUTOUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Classify',
    full_name='session_manager.SessionManager.Classify',
    index=3,
    containing_service=None,
    input_type=_CLASSIFYINPUT,
    output_type=_CLASSIFYOUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONMANAGER)

DESCRIPTOR.services_by_name['SessionManager'] = _SESSIONMANAGER

# @@protoc_insertion_point(module_scope)
