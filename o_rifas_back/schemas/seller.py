from marshmallow import Schema, fields

from schemas.table import (
    NumbersViewSchema,
)

class SellerSchema(Schema):
    avaiable_numbers = fields.Int(dump_only=True)
    contact = fields.Str(dump_only=True)
    seller_name = fields.Str(dump_only=True)
    sold_numbers = fields.Int(dump_only=True)
    numbers = fields.Nested(NumbersViewSchema, many=True)
    pix = fields.Str(dump_only=True)
