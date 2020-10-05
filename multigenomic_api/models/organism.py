from mongoengine import fields
from mongoengine import DynamicDocument
from .base import Base


class Organism(DynamicDocument, Base):
    description = fields.StringField(required=True)
    note = fields.StringField(required=False)
    sequence = fields.StringField(required=True)
    url = fields.StringField(required=False)

    def __init__(self, **kwargs):
        super().__init__()
