from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .base import Base


class Members(DynamicEmbeddedDocument):
    genes = fields.ListField(fields.StringField(), required=False)
    products = fields.ListField(fields.StringField(), required=False)
    meta = {'abstract': True}


class Term(DynamicDocument, Base):
    description = fields.StringField(required=False)
    has = fields.ListField(fields.StringField(), required=False)
    is_a = fields.ListField(fields.StringField(), required=False, db_field="isA")
    members = fields.EmbeddedDocumentField(Members, required=False)
    url = fields.StringField(required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
