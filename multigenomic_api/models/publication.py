from mongoengine import fields
from mongoengine import DynamicDocument
from .base import Base


class Publication(DynamicDocument, Base):
    authors = fields.ListField(fields.StringField(), required=False)
    pmid = fields.StringField(required=False)
    source = fields.StringField(required=False)
    title = fields.StringField(required=False)
    url = fields.StringField(required=False)
    year = fields.IntField(required=False)