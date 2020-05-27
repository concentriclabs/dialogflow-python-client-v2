# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2/proto/webhook.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dialogflow_v2.proto import (
    context_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2,
)
from dialogflow_v2.proto import (
    intent_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_intent__pb2,
)
from dialogflow_v2.proto import (
    session_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__pb2,
)
from dialogflow_v2.proto import (
    session_entity_type_pb2 as google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__entity__type__pb2,
)
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/dialogflow_v2/proto/webhook.proto",
    package="google.cloud.dialogflow.v2",
    syntax="proto3",
    serialized_options=_b(
        "\n\036com.google.cloud.dialogflow.v2B\014WebhookProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2"
    ),
    serialized_pb=_b(
        '\n.google/cloud/dialogflow_v2/proto/webhook.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a.google/cloud/dialogflow_v2/proto/context.proto\x1a-google/cloud/dialogflow_v2/proto/intent.proto\x1a.google/cloud/dialogflow_v2/proto/session.proto\x1a:google/cloud/dialogflow_v2/proto/session_entity_type.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto"\xd6\x01\n\x0eWebhookRequest\x12\x0f\n\x07session\x18\x04 \x01(\t\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12=\n\x0cquery_result\x18\x02 \x01(\x0b\x32\'.google.cloud.dialogflow.v2.QueryResult\x12_\n\x1eoriginal_detect_intent_request\x18\x03 \x01(\x0b\x32\x37.google.cloud.dialogflow.v2.OriginalDetectIntentRequest"\x80\x03\n\x0fWebhookResponse\x12\x18\n\x10\x66ulfillment_text\x18\x01 \x01(\t\x12H\n\x14\x66ulfillment_messages\x18\x02 \x03(\x0b\x32*.google.cloud.dialogflow.v2.Intent.Message\x12\x0e\n\x06source\x18\x03 \x01(\t\x12(\n\x07payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12<\n\x0foutput_contexts\x18\x05 \x03(\x0b\x32#.google.cloud.dialogflow.v2.Context\x12\x44\n\x14\x66ollowup_event_input\x18\x06 \x01(\x0b\x32&.google.cloud.dialogflow.v2.EventInput\x12K\n\x14session_entity_types\x18\n \x03(\x0b\x32-.google.cloud.dialogflow.v2.SessionEntityType"h\n\x1bOriginalDetectIntentRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12(\n\x07payload\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructB\x9b\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x0cWebhookProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_intent__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__pb2.DESCRIPTOR,
        google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__entity__type__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_WEBHOOKREQUEST = _descriptor.Descriptor(
    name="WebhookRequest",
    full_name="google.cloud.dialogflow.v2.WebhookRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="session",
            full_name="google.cloud.dialogflow.v2.WebhookRequest.session",
            index=0,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="response_id",
            full_name="google.cloud.dialogflow.v2.WebhookRequest.response_id",
            index=1,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="query_result",
            full_name="google.cloud.dialogflow.v2.WebhookRequest.query_result",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="original_detect_intent_request",
            full_name="google.cloud.dialogflow.v2.WebhookRequest.original_detect_intent_request",
            index=3,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=342,
    serialized_end=556,
)


_WEBHOOKRESPONSE = _descriptor.Descriptor(
    name="WebhookResponse",
    full_name="google.cloud.dialogflow.v2.WebhookResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="fulfillment_text",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.fulfillment_text",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fulfillment_messages",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.fulfillment_messages",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="source",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.source",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.payload",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="output_contexts",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.output_contexts",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="followup_event_input",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.followup_event_input",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="session_entity_types",
            full_name="google.cloud.dialogflow.v2.WebhookResponse.session_entity_types",
            index=6,
            number=10,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=559,
    serialized_end=943,
)


_ORIGINALDETECTINTENTREQUEST = _descriptor.Descriptor(
    name="OriginalDetectIntentRequest",
    full_name="google.cloud.dialogflow.v2.OriginalDetectIntentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="source",
            full_name="google.cloud.dialogflow.v2.OriginalDetectIntentRequest.source",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="version",
            full_name="google.cloud.dialogflow.v2.OriginalDetectIntentRequest.version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="payload",
            full_name="google.cloud.dialogflow.v2.OriginalDetectIntentRequest.payload",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=945,
    serialized_end=1049,
)

_WEBHOOKREQUEST.fields_by_name[
    "query_result"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__pb2._QUERYRESULT
)
_WEBHOOKREQUEST.fields_by_name[
    "original_detect_intent_request"
].message_type = _ORIGINALDETECTINTENTREQUEST
_WEBHOOKRESPONSE.fields_by_name[
    "fulfillment_messages"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_intent__pb2._INTENT_MESSAGE
)
_WEBHOOKRESPONSE.fields_by_name[
    "payload"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_WEBHOOKRESPONSE.fields_by_name[
    "output_contexts"
].message_type = google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_context__pb2._CONTEXT
_WEBHOOKRESPONSE.fields_by_name[
    "followup_event_input"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__pb2._EVENTINPUT
)
_WEBHOOKRESPONSE.fields_by_name[
    "session_entity_types"
].message_type = (
    google_dot_cloud_dot_dialogflow__v2_dot_proto_dot_session__entity__type__pb2._SESSIONENTITYTYPE
)
_ORIGINALDETECTINTENTREQUEST.fields_by_name[
    "payload"
].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name["WebhookRequest"] = _WEBHOOKREQUEST
DESCRIPTOR.message_types_by_name["WebhookResponse"] = _WEBHOOKRESPONSE
DESCRIPTOR.message_types_by_name[
    "OriginalDetectIntentRequest"
] = _ORIGINALDETECTINTENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WebhookRequest = _reflection.GeneratedProtocolMessageType(
    "WebhookRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_WEBHOOKREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.webhook_pb2",
        __doc__="""The request message for a webhook call.
  Attributes:
      session:
          The unique identifier of detectIntent request session. Can be
          used to identify end-user inside webhook implementation.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``,
          or ``projects/<Project ID>/agent/environments/<Environment
          ID>/users/<User ID>/sessions/<Session ID>``.
      response_id:
          The unique identifier of the response. Contains the same value
          as ``[Streaming]DetectIntentResponse.response_id``.
      query_result:
          The result of the conversational query or event processing.
          Contains the same value as
          ``[Streaming]DetectIntentResponse.query_result``.
      original_detect_intent_request:
          Optional. The contents of the original request that was passed
          to ``[Streaming]DetectIntent`` call.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.WebhookRequest)
    ),
)
_sym_db.RegisterMessage(WebhookRequest)

WebhookResponse = _reflection.GeneratedProtocolMessageType(
    "WebhookResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_WEBHOOKRESPONSE,
        __module__="google.cloud.dialogflow_v2.proto.webhook_pb2",
        __doc__="""The response message for a webhook call.  This response is validated
  by the Dialogflow server. If validation fails, an error will be
  returned in the [QueryResult.diagnostic\_info][google.cloud.dialogflow
  .v2.QueryResult.diagnostic\_info] field. Setting JSON fields to an
  empty value with the wrong type is a common error. To avoid this
  error:  -  Use ``""`` for empty strings -  Use ``{}`` or ``null`` for
  empty objects -  Use ``[]`` or ``null`` for empty arrays  For more
  information, see the `Protocol Buffers Language Guide
  <https://developers.google.com/protocol-buffers/docs/proto3#json>`__.
  Attributes:
      fulfillment_text:
          Optional. The text to be shown on the screen. This value is
          passed directly to ``QueryResult.fulfillment_text``.
      fulfillment_messages:
          Optional. The collection of rich messages to present to the
          user. This value is passed directly to
          ``QueryResult.fulfillment_messages``.
      source:
          Optional. This value is passed directly to
          ``QueryResult.webhook_source``.
      payload:
          Optional. This value is passed directly to
          ``QueryResult.webhook_payload``. See the related
          ``fulfillment_messages[i].payload field``, which may be used
          as an alternative to this field.  This field can be used for
          Actions on Google responses. It should have a structure
          similar to the JSON message shown here. For more information,
          see `Actions on Google Webhook Format
          <https://developers.google.com/actions/dialogflow/webhook>`__
          .. raw:: html     <pre>{      "google": {
          "expectUserResponse": true,        "richResponse": {
          "items": [            {              "simpleResponse": {
          "textToSpeech": "this is a simple response"              }
          }          ]        }      }    }</pre>
      output_contexts:
          Optional. The collection of output contexts. This value is
          passed directly to ``QueryResult.output_contexts``.
      followup_event_input:
          Optional. Makes the platform immediately invoke another
          ``DetectIntent`` call internally with the specified event as
          input. When this field is set, Dialogflow ignores the
          ``fulfillment_text``, ``fulfillment_messages``, and
          ``payload`` fields.
      session_entity_types:
          Optional. Additional session entity types to replace or extend
          developer entity types with. The entity synonyms apply to all
          languages and persist for the session of this query. Setting
          the session entity types inside webhook overwrites the session
          entity types that have been set through
          ``DetectIntentRequest.query_params.session_entity_types``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.WebhookResponse)
    ),
)
_sym_db.RegisterMessage(WebhookResponse)

OriginalDetectIntentRequest = _reflection.GeneratedProtocolMessageType(
    "OriginalDetectIntentRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ORIGINALDETECTINTENTREQUEST,
        __module__="google.cloud.dialogflow_v2.proto.webhook_pb2",
        __doc__="""Represents the contents of the original request that was passed to the
  ``[Streaming]DetectIntent`` call.
  Attributes:
      source:
          The source of this request, e.g., ``google``, ``facebook``,
          ``slack``. It is set by Dialogflow-owned servers.
      version:
          Optional. The version of the protocol used for this request.
          This field is AoG-specific.
      payload:
          Optional. This field is set to the value of the
          ``QueryParameters.payload`` field passed in the request. Some
          integrations that query a Dialogflow agent may provide
          additional information in the payload.  In particular for the
          Telephony Gateway this field has the form:  .. raw:: html
          <pre>{     "telephony": {       "caller_id": "+18558363987"
          }    }</pre>  Note: The caller ID field (``caller_id``) will
          be redacted for Standard Edition agents and populated with the
          caller ID in `E.164 format
          <https://en.wikipedia.org/wiki/E.164>`__ for Enterprise
          Edition agents.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.OriginalDetectIntentRequest)
    ),
)
_sym_db.RegisterMessage(OriginalDetectIntentRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
