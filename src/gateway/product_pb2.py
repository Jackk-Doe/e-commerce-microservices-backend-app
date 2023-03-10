# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: product.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproduct.proto\x12\x07product\"\x06\n\x04Null\"\x13\n\x02Id\x12\r\n\x05value\x18\x01 \x01(\t\"\x17\n\x06Status\x12\r\n\x05value\x18\x01 \x01(\x08\"g\n\x10ProductInputForm\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tseller_id\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x05\"T\n\x13ProductIdWithUserId\x12\x1f\n\nproduct_id\x18\x01 \x01(\x0b\x32\x0b.product.Id\x12\x1c\n\x07user_id\x18\x02 \x01(\x0b\x32\x0b.product.Id\"z\n\x16ProductUpdateInputForm\x12)\n\x03ids\x18\x01 \x01(\x0b\x32\x1c.product.ProductIdWithUserId\x12\x35\n\x12productFormRequest\x18\x02 \x01(\x0b\x32\x19.product.ProductInputForm\"\x81\x01\n\nProductDTO\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tseller_id\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x02\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x05\x12\n\n\x02id\x18\x06 \x01(\t\x12\x12\n\nimage_path\x18\x07 \x01(\t\"L\n\x10ProductListInput\x12\x11\n\x04page\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05limit\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x07\n\x05_pageB\x08\n\x06_limit\"Y\n\x0eProductListDTO\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x12\n\ntotal_page\x18\x02 \x01(\x05\x12%\n\x08products\x18\x03 \x03(\x0b\x32\x13.product.ProductDTO2\xc8\x02\n\x07Product\x12\x41\n\x0bGetProducts\x12\x19.product.ProductListInput\x1a\x17.product.ProductListDTO\x12\x32\n\x0eGetProductById\x12\x0b.product.Id\x1a\x13.product.ProductDTO\x12?\n\rCreateProduct\x12\x19.product.ProductInputForm\x1a\x13.product.ProductDTO\x12\x45\n\rUpdateProduct\x12\x1f.product.ProductUpdateInputForm\x1a\x13.product.ProductDTO\x12>\n\rDeleteProduct\x12\x1c.product.ProductIdWithUserId\x1a\x0f.product.Statusb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'product_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NULL._serialized_start=26
  _NULL._serialized_end=32
  _ID._serialized_start=34
  _ID._serialized_end=53
  _STATUS._serialized_start=55
  _STATUS._serialized_end=78
  _PRODUCTINPUTFORM._serialized_start=80
  _PRODUCTINPUTFORM._serialized_end=183
  _PRODUCTIDWITHUSERID._serialized_start=185
  _PRODUCTIDWITHUSERID._serialized_end=269
  _PRODUCTUPDATEINPUTFORM._serialized_start=271
  _PRODUCTUPDATEINPUTFORM._serialized_end=393
  _PRODUCTDTO._serialized_start=396
  _PRODUCTDTO._serialized_end=525
  _PRODUCTLISTINPUT._serialized_start=527
  _PRODUCTLISTINPUT._serialized_end=603
  _PRODUCTLISTDTO._serialized_start=605
  _PRODUCTLISTDTO._serialized_end=694
  _PRODUCT._serialized_start=697
  _PRODUCT._serialized_end=1025
# @@protoc_insertion_point(module_scope)
