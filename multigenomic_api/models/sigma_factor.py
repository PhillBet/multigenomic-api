from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .biological_base import BiologicalBase


class SigmaFactor(DynamicDocument, BiologicalBase):
    gene_id = fields.StringField(required=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'sigmaFactor'}