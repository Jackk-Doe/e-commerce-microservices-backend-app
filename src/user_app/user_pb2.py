# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\t\"\x16\n\x05Token\x12\r\n\x05value\x18\x01 \x01(\t\"?\n\x0eUserSignUpForm\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"0\n\rUserLogInForm\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"5\n\x07UserDTO\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t2\xa7\x01\n\x04User\x12+\n\x05LogIn\x12\x13.user.UserLogInForm\x1a\r.user.UserDTO\x12-\n\x06SignUp\x12\x14.user.UserSignUpForm\x1a\r.user.UserDTO\x12#\n\x05GetMe\x12\x0b.user.Token\x1a\r.user.UserDTO\x12\x1e\n\x05GetId\x12\x0b.user.Token\x1a\x08.user.Idb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ID._serialized_start=20
  _ID._serialized_end=39
  _TOKEN._serialized_start=41
  _TOKEN._serialized_end=63
  _USERSIGNUPFORM._serialized_start=65
  _USERSIGNUPFORM._serialized_end=128
  _USERLOGINFORM._serialized_start=130
  _USERLOGINFORM._serialized_end=178
  _USERDTO._serialized_start=180
  _USERDTO._serialized_end=233
  _USER._serialized_start=236
  _USER._serialized_end=403
# @@protoc_insertion_point(module_scope)
