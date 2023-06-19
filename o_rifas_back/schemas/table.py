from marshmallow import Schema, fields

class NumbersViewSchema(Schema):
    number = fields.Str(dump_only=True)
    sold = fields.Str(dump_only=True)