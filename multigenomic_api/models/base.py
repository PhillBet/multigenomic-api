from mongoengine import fields


class Base:
    id = fields.StringField(required=True, db_field="_id", primary_key=True)
    internal_comment = fields.StringField(required=False, db_field="internalComment")
    name = fields.StringField(required=False)
    note = fields.StringField(required=False)

    meta = {'abstract': True}