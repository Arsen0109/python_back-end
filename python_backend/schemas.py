from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    password = fields.Str(required=True)
    admin = fields.Bool()


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)


class CategoryResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    user_id = fields.Int(required=True)


class NoteQuerySchema(Schema):
    user_id = fields.Int(required=True)
    category_id = fields.Int()


class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    currency_id = fields.Int()
    price = fields.Float(required=True)
