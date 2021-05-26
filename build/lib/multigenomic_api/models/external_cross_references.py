from mongoengine import DynamicDocument
from mongoengine import fields

from .base import Base


class ExternalCrossReferences(DynamicDocument, Base):
    description = fields.StringField(required=False)
    url = fields.StringField(required=False)

    meta = {'collection': 'externalCrossReferences'}
