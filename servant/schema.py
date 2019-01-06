"""All JSON schemas used at project."""

from marshmallow import Schema, fields


class RequestSchema(Schema):
    """Request JSON schema."""

    text = fields.String(description='Text to be processed')


class EntitySchema(Schema):
    """Recognized entity JSON schema."""

    text = fields.String()
    type = fields.String()
    begin_offset = fields.Integer()
    end_offset = fields.Integer()


class ResponseSchema(Schema):
    """Response JSON schema."""

    tokens = fields.List(
        fields.String,
        description='List of words in text',
        example=['Hello', 'world', '!']
    )
    entities = fields.Nested(EntitySchema, many=True)
