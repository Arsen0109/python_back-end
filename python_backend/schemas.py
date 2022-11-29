from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)


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
