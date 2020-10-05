from mongoengine import fields
from mongoengine import DynamicDocument

from .base import Base


class Evidence(DynamicDocument, Base):
    code = fields.StringField(required=False)
    pertains_to = fields.ListField(fields.StringField(), required=False, db_field="pertainsTo")
    type_object = fields.ListField(fields.StringField(), required=False, db_field="typeObject")