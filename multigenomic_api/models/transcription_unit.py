from mongoengine import fields
from mongoengine import DynamicDocument

from .biological_base import BiologicalBase


class TranscriptionUnit(DynamicDocument, BiologicalBase):
    gene_ids = fields.ListField(fields.StringField(), required=True)
    promoter_ids = fields.ListField(fields.StringField(), required=False)
    operon_id = fields.StringField(required=True)
    terminator_ids = fields.ListField(fields.StringField(), required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'transcriptionUnit'}