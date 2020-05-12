# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nlp_position_profile.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import profile_pb2 as profile__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nlp_position_profile.proto',
  package='nlpPositionProfile',
  syntax='proto3',
  serialized_options=_b('Z\005proto'),
  serialized_pb=_b('\n\x1anlp_position_profile.proto\x12\x12nlpPositionProfile\x1a\rprofile.proto\"m\n\x14\x43VAggregationRequest\x12\x10\n\x08job_func\x18\x01 \x01(\t\x12\x0e\n\x06plc_id\x18\x02 \x01(\x05\x12\x33\n\twork_dura\x18\x03 \x01(\x0e\x32 .nlpPositionProfile.WorkDuraType\"{\n\x15\x43VAggregationResponse\x12\x0e\n\x06\x65rr_no\x18\x01 \x01(\x05\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\x12\x41\n\x07results\x18\x03 \x01(\x0b\x32\x30.nlpPositionProfile.CVAggregationResponseResults\"S\n\x1c\x43VAggregationResponseResults\x12\x33\n\x14upon_profile_from_cv\x18\x01 \x01(\x0b\x32\x15.profile.Axis1Profile\"f\n\x0eJobDescription\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x13\n\x0brequirement\x18\x02 \x01(\t\x12\x18\n\x10\x63orporation_name\x18\x03 \x01(\t\x12\x10\n\x08job_func\x18\x04 \x01(\t\"C\n\x11JDAnalysisRequest\x12.\n\x02jd\x18\x01 \x01(\x0b\x32\".nlpPositionProfile.JobDescription\"u\n\x12JDAnalysisResponse\x12\x0e\n\x06\x65rr_no\x18\x01 \x01(\x05\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\x12>\n\x07results\x18\x03 \x01(\x0b\x32-.nlpPositionProfile.JDAnalysisResponseResults\"s\n\x19JDAnalysisResponseResults\x12*\n\x0b\x64\x65scription\x18\x01 \x01(\x0b\x32\x15.profile.Axis1Profile\x12*\n\x0brequirement\x18\x02 \x01(\x0b\x32\x15.profile.Axis1Profile\"\\\n\x13UnderProfileRequest\x12\x10\n\x08job_func\x18\x01 \x01(\t\x12\x33\n\x14upon_profile_from_cv\x18\x02 \x01(\x0b\x32\x15.profile.Axis1Profile\"y\n\x14UnderProfileResponse\x12\x0e\n\x06\x65rr_no\x18\x01 \x01(\x05\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\x12@\n\x07results\x18\x03 \x01(\x0b\x32/.nlpPositionProfile.UnderProfileResponseResults\"K\n\x1bUnderProfileResponseResults\x12,\n\runder_profile\x18\x01 \x01(\x0b\x32\x15.profile.Axis1Profile\"K\n\x1bGenAxis2Axis3ProfileRequest\x12,\n\raxis1_profile\x18\x01 \x01(\x0b\x32\x15.profile.Axis1Profile\"\x89\x01\n\x1cGenAxis2Axis3ProfileResponse\x12\x0e\n\x06\x65rr_no\x18\x01 \x01(\x05\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\x12H\n\x07results\x18\x03 \x01(\x0b\x32\x37.nlpPositionProfile.GenAxis2Axis3ProfileResponseResults\"M\n#GenAxis2Axis3ProfileResponseResults\x12&\n\x0c\x66ull_profile\x18\x01 \x01(\x0b\x32\x10.profile.Profile*e\n\x0cWorkDuraType\x12\x12\n\x0e\x42\x45LOW_ONE_YEAR\x10\x00\x12\x13\n\x0fONE2THREE_YEARS\x10\x01\x12\x14\n\x10THREE2FIVE_YEARS\x10\x02\x12\x16\n\x12\x42\x45YOUND_FIVE_YEARS\x10\x03\x32q\n\rCVAggregation\x12`\n\x07\x43ompute\x12(.nlpPositionProfile.CVAggregationRequest\x1a).nlpPositionProfile.CVAggregationResponse\"\x00\x32h\n\nJDAnalysis\x12Z\n\x07\x43ompute\x12%.nlpPositionProfile.JDAnalysisRequest\x1a&.nlpPositionProfile.JDAnalysisResponse\"\x00\x32n\n\x0cUnderProfile\x12^\n\x07\x43ompute\x12\'.nlpPositionProfile.UnderProfileRequest\x1a(.nlpPositionProfile.UnderProfileResponse\"\x00\x32\x86\x01\n\x14GenAxis2Axis3Profile\x12n\n\x07\x43ompute\x12/.nlpPositionProfile.GenAxis2Axis3ProfileRequest\x1a\x30.nlpPositionProfile.GenAxis2Axis3ProfileResponse\"\x00\x42\x07Z\x05protob\x06proto3')
  ,
  dependencies=[profile__pb2.DESCRIPTOR,])

_WORKDURATYPE = _descriptor.EnumDescriptor(
  name='WorkDuraType',
  full_name='nlpPositionProfile.WorkDuraType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BELOW_ONE_YEAR', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE2THREE_YEARS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THREE2FIVE_YEARS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEYOUND_FIVE_YEARS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1385,
  serialized_end=1486,
)
_sym_db.RegisterEnumDescriptor(_WORKDURATYPE)

WorkDuraType = enum_type_wrapper.EnumTypeWrapper(_WORKDURATYPE)
BELOW_ONE_YEAR = 0
ONE2THREE_YEARS = 1
THREE2FIVE_YEARS = 2
BEYOUND_FIVE_YEARS = 3



_CVAGGREGATIONREQUEST = _descriptor.Descriptor(
  name='CVAggregationRequest',
  full_name='nlpPositionProfile.CVAggregationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_func', full_name='nlpPositionProfile.CVAggregationRequest.job_func', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plc_id', full_name='nlpPositionProfile.CVAggregationRequest.plc_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='work_dura', full_name='nlpPositionProfile.CVAggregationRequest.work_dura', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=65,
  serialized_end=174,
)


_CVAGGREGATIONRESPONSE = _descriptor.Descriptor(
  name='CVAggregationResponse',
  full_name='nlpPositionProfile.CVAggregationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_no', full_name='nlpPositionProfile.CVAggregationResponse.err_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='nlpPositionProfile.CVAggregationResponse.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='nlpPositionProfile.CVAggregationResponse.results', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=176,
  serialized_end=299,
)


_CVAGGREGATIONRESPONSERESULTS = _descriptor.Descriptor(
  name='CVAggregationResponseResults',
  full_name='nlpPositionProfile.CVAggregationResponseResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='upon_profile_from_cv', full_name='nlpPositionProfile.CVAggregationResponseResults.upon_profile_from_cv', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=301,
  serialized_end=384,
)


_JOBDESCRIPTION = _descriptor.Descriptor(
  name='JobDescription',
  full_name='nlpPositionProfile.JobDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='nlpPositionProfile.JobDescription.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirement', full_name='nlpPositionProfile.JobDescription.requirement', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='corporation_name', full_name='nlpPositionProfile.JobDescription.corporation_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_func', full_name='nlpPositionProfile.JobDescription.job_func', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=386,
  serialized_end=488,
)


_JDANALYSISREQUEST = _descriptor.Descriptor(
  name='JDAnalysisRequest',
  full_name='nlpPositionProfile.JDAnalysisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jd', full_name='nlpPositionProfile.JDAnalysisRequest.jd', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=490,
  serialized_end=557,
)


_JDANALYSISRESPONSE = _descriptor.Descriptor(
  name='JDAnalysisResponse',
  full_name='nlpPositionProfile.JDAnalysisResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_no', full_name='nlpPositionProfile.JDAnalysisResponse.err_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='nlpPositionProfile.JDAnalysisResponse.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='nlpPositionProfile.JDAnalysisResponse.results', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=559,
  serialized_end=676,
)


_JDANALYSISRESPONSERESULTS = _descriptor.Descriptor(
  name='JDAnalysisResponseResults',
  full_name='nlpPositionProfile.JDAnalysisResponseResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='nlpPositionProfile.JDAnalysisResponseResults.description', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requirement', full_name='nlpPositionProfile.JDAnalysisResponseResults.requirement', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=678,
  serialized_end=793,
)


_UNDERPROFILEREQUEST = _descriptor.Descriptor(
  name='UnderProfileRequest',
  full_name='nlpPositionProfile.UnderProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_func', full_name='nlpPositionProfile.UnderProfileRequest.job_func', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upon_profile_from_cv', full_name='nlpPositionProfile.UnderProfileRequest.upon_profile_from_cv', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=795,
  serialized_end=887,
)


_UNDERPROFILERESPONSE = _descriptor.Descriptor(
  name='UnderProfileResponse',
  full_name='nlpPositionProfile.UnderProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_no', full_name='nlpPositionProfile.UnderProfileResponse.err_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='nlpPositionProfile.UnderProfileResponse.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='nlpPositionProfile.UnderProfileResponse.results', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=889,
  serialized_end=1010,
)


_UNDERPROFILERESPONSERESULTS = _descriptor.Descriptor(
  name='UnderProfileResponseResults',
  full_name='nlpPositionProfile.UnderProfileResponseResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='under_profile', full_name='nlpPositionProfile.UnderProfileResponseResults.under_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1012,
  serialized_end=1087,
)


_GENAXIS2AXIS3PROFILEREQUEST = _descriptor.Descriptor(
  name='GenAxis2Axis3ProfileRequest',
  full_name='nlpPositionProfile.GenAxis2Axis3ProfileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='axis1_profile', full_name='nlpPositionProfile.GenAxis2Axis3ProfileRequest.axis1_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1089,
  serialized_end=1164,
)


_GENAXIS2AXIS3PROFILERESPONSE = _descriptor.Descriptor(
  name='GenAxis2Axis3ProfileResponse',
  full_name='nlpPositionProfile.GenAxis2Axis3ProfileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='err_no', full_name='nlpPositionProfile.GenAxis2Axis3ProfileResponse.err_no', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='nlpPositionProfile.GenAxis2Axis3ProfileResponse.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='nlpPositionProfile.GenAxis2Axis3ProfileResponse.results', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1167,
  serialized_end=1304,
)


_GENAXIS2AXIS3PROFILERESPONSERESULTS = _descriptor.Descriptor(
  name='GenAxis2Axis3ProfileResponseResults',
  full_name='nlpPositionProfile.GenAxis2Axis3ProfileResponseResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_profile', full_name='nlpPositionProfile.GenAxis2Axis3ProfileResponseResults.full_profile', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1306,
  serialized_end=1383,
)

_CVAGGREGATIONREQUEST.fields_by_name['work_dura'].enum_type = _WORKDURATYPE
_CVAGGREGATIONRESPONSE.fields_by_name['results'].message_type = _CVAGGREGATIONRESPONSERESULTS
_CVAGGREGATIONRESPONSERESULTS.fields_by_name['upon_profile_from_cv'].message_type = profile__pb2._AXIS1PROFILE
_JDANALYSISREQUEST.fields_by_name['jd'].message_type = _JOBDESCRIPTION
_JDANALYSISRESPONSE.fields_by_name['results'].message_type = _JDANALYSISRESPONSERESULTS
_JDANALYSISRESPONSERESULTS.fields_by_name['description'].message_type = profile__pb2._AXIS1PROFILE
_JDANALYSISRESPONSERESULTS.fields_by_name['requirement'].message_type = profile__pb2._AXIS1PROFILE
_UNDERPROFILEREQUEST.fields_by_name['upon_profile_from_cv'].message_type = profile__pb2._AXIS1PROFILE
_UNDERPROFILERESPONSE.fields_by_name['results'].message_type = _UNDERPROFILERESPONSERESULTS
_UNDERPROFILERESPONSERESULTS.fields_by_name['under_profile'].message_type = profile__pb2._AXIS1PROFILE
_GENAXIS2AXIS3PROFILEREQUEST.fields_by_name['axis1_profile'].message_type = profile__pb2._AXIS1PROFILE
_GENAXIS2AXIS3PROFILERESPONSE.fields_by_name['results'].message_type = _GENAXIS2AXIS3PROFILERESPONSERESULTS
_GENAXIS2AXIS3PROFILERESPONSERESULTS.fields_by_name['full_profile'].message_type = profile__pb2._PROFILE
DESCRIPTOR.message_types_by_name['CVAggregationRequest'] = _CVAGGREGATIONREQUEST
DESCRIPTOR.message_types_by_name['CVAggregationResponse'] = _CVAGGREGATIONRESPONSE
DESCRIPTOR.message_types_by_name['CVAggregationResponseResults'] = _CVAGGREGATIONRESPONSERESULTS
DESCRIPTOR.message_types_by_name['JobDescription'] = _JOBDESCRIPTION
DESCRIPTOR.message_types_by_name['JDAnalysisRequest'] = _JDANALYSISREQUEST
DESCRIPTOR.message_types_by_name['JDAnalysisResponse'] = _JDANALYSISRESPONSE
DESCRIPTOR.message_types_by_name['JDAnalysisResponseResults'] = _JDANALYSISRESPONSERESULTS
DESCRIPTOR.message_types_by_name['UnderProfileRequest'] = _UNDERPROFILEREQUEST
DESCRIPTOR.message_types_by_name['UnderProfileResponse'] = _UNDERPROFILERESPONSE
DESCRIPTOR.message_types_by_name['UnderProfileResponseResults'] = _UNDERPROFILERESPONSERESULTS
DESCRIPTOR.message_types_by_name['GenAxis2Axis3ProfileRequest'] = _GENAXIS2AXIS3PROFILEREQUEST
DESCRIPTOR.message_types_by_name['GenAxis2Axis3ProfileResponse'] = _GENAXIS2AXIS3PROFILERESPONSE
DESCRIPTOR.message_types_by_name['GenAxis2Axis3ProfileResponseResults'] = _GENAXIS2AXIS3PROFILERESPONSERESULTS
DESCRIPTOR.enum_types_by_name['WorkDuraType'] = _WORKDURATYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CVAggregationRequest = _reflection.GeneratedProtocolMessageType('CVAggregationRequest', (_message.Message,), dict(
  DESCRIPTOR = _CVAGGREGATIONREQUEST,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.CVAggregationRequest)
  ))
_sym_db.RegisterMessage(CVAggregationRequest)

CVAggregationResponse = _reflection.GeneratedProtocolMessageType('CVAggregationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CVAGGREGATIONRESPONSE,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.CVAggregationResponse)
  ))
_sym_db.RegisterMessage(CVAggregationResponse)

CVAggregationResponseResults = _reflection.GeneratedProtocolMessageType('CVAggregationResponseResults', (_message.Message,), dict(
  DESCRIPTOR = _CVAGGREGATIONRESPONSERESULTS,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.CVAggregationResponseResults)
  ))
_sym_db.RegisterMessage(CVAggregationResponseResults)

JobDescription = _reflection.GeneratedProtocolMessageType('JobDescription', (_message.Message,), dict(
  DESCRIPTOR = _JOBDESCRIPTION,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.JobDescription)
  ))
_sym_db.RegisterMessage(JobDescription)

JDAnalysisRequest = _reflection.GeneratedProtocolMessageType('JDAnalysisRequest', (_message.Message,), dict(
  DESCRIPTOR = _JDANALYSISREQUEST,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.JDAnalysisRequest)
  ))
_sym_db.RegisterMessage(JDAnalysisRequest)

JDAnalysisResponse = _reflection.GeneratedProtocolMessageType('JDAnalysisResponse', (_message.Message,), dict(
  DESCRIPTOR = _JDANALYSISRESPONSE,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.JDAnalysisResponse)
  ))
_sym_db.RegisterMessage(JDAnalysisResponse)

JDAnalysisResponseResults = _reflection.GeneratedProtocolMessageType('JDAnalysisResponseResults', (_message.Message,), dict(
  DESCRIPTOR = _JDANALYSISRESPONSERESULTS,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.JDAnalysisResponseResults)
  ))
_sym_db.RegisterMessage(JDAnalysisResponseResults)

UnderProfileRequest = _reflection.GeneratedProtocolMessageType('UnderProfileRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNDERPROFILEREQUEST,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.UnderProfileRequest)
  ))
_sym_db.RegisterMessage(UnderProfileRequest)

UnderProfileResponse = _reflection.GeneratedProtocolMessageType('UnderProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNDERPROFILERESPONSE,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.UnderProfileResponse)
  ))
_sym_db.RegisterMessage(UnderProfileResponse)

UnderProfileResponseResults = _reflection.GeneratedProtocolMessageType('UnderProfileResponseResults', (_message.Message,), dict(
  DESCRIPTOR = _UNDERPROFILERESPONSERESULTS,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.UnderProfileResponseResults)
  ))
_sym_db.RegisterMessage(UnderProfileResponseResults)

GenAxis2Axis3ProfileRequest = _reflection.GeneratedProtocolMessageType('GenAxis2Axis3ProfileRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENAXIS2AXIS3PROFILEREQUEST,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.GenAxis2Axis3ProfileRequest)
  ))
_sym_db.RegisterMessage(GenAxis2Axis3ProfileRequest)

GenAxis2Axis3ProfileResponse = _reflection.GeneratedProtocolMessageType('GenAxis2Axis3ProfileResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENAXIS2AXIS3PROFILERESPONSE,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.GenAxis2Axis3ProfileResponse)
  ))
_sym_db.RegisterMessage(GenAxis2Axis3ProfileResponse)

GenAxis2Axis3ProfileResponseResults = _reflection.GeneratedProtocolMessageType('GenAxis2Axis3ProfileResponseResults', (_message.Message,), dict(
  DESCRIPTOR = _GENAXIS2AXIS3PROFILERESPONSERESULTS,
  __module__ = 'nlp_position_profile_pb2'
  # @@protoc_insertion_point(class_scope:nlpPositionProfile.GenAxis2Axis3ProfileResponseResults)
  ))
_sym_db.RegisterMessage(GenAxis2Axis3ProfileResponseResults)


DESCRIPTOR._options = None

_CVAGGREGATION = _descriptor.ServiceDescriptor(
  name='CVAggregation',
  full_name='nlpPositionProfile.CVAggregation',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1488,
  serialized_end=1601,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='nlpPositionProfile.CVAggregation.Compute',
    index=0,
    containing_service=None,
    input_type=_CVAGGREGATIONREQUEST,
    output_type=_CVAGGREGATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CVAGGREGATION)

DESCRIPTOR.services_by_name['CVAggregation'] = _CVAGGREGATION


_JDANALYSIS = _descriptor.ServiceDescriptor(
  name='JDAnalysis',
  full_name='nlpPositionProfile.JDAnalysis',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1603,
  serialized_end=1707,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='nlpPositionProfile.JDAnalysis.Compute',
    index=0,
    containing_service=None,
    input_type=_JDANALYSISREQUEST,
    output_type=_JDANALYSISRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JDANALYSIS)

DESCRIPTOR.services_by_name['JDAnalysis'] = _JDANALYSIS


_UNDERPROFILE = _descriptor.ServiceDescriptor(
  name='UnderProfile',
  full_name='nlpPositionProfile.UnderProfile',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=1709,
  serialized_end=1819,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='nlpPositionProfile.UnderProfile.Compute',
    index=0,
    containing_service=None,
    input_type=_UNDERPROFILEREQUEST,
    output_type=_UNDERPROFILERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_UNDERPROFILE)

DESCRIPTOR.services_by_name['UnderProfile'] = _UNDERPROFILE


_GENAXIS2AXIS3PROFILE = _descriptor.ServiceDescriptor(
  name='GenAxis2Axis3Profile',
  full_name='nlpPositionProfile.GenAxis2Axis3Profile',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  serialized_start=1822,
  serialized_end=1956,
  methods=[
  _descriptor.MethodDescriptor(
    name='Compute',
    full_name='nlpPositionProfile.GenAxis2Axis3Profile.Compute',
    index=0,
    containing_service=None,
    input_type=_GENAXIS2AXIS3PROFILEREQUEST,
    output_type=_GENAXIS2AXIS3PROFILERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENAXIS2AXIS3PROFILE)

DESCRIPTOR.services_by_name['GenAxis2Axis3Profile'] = _GENAXIS2AXIS3PROFILE

# @@protoc_insertion_point(module_scope)