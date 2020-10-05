from mongoengine import DynamicDocument
from mongoengine import fields

from .base import Base


class ExternalCrossReference(DynamicDocument, Base):
    description = fields.StringField(required=False)
    url = fields.StringField(required=False)

    meta = {'collection': 'externalCrossReference'}
