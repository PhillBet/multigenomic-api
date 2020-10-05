from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .biological_base import BiologicalBase


class Genes(DynamicEmbeddedDocument):
    gene_id = fields.StringField()
    left_end_position = fields.IntField(db_field="leftEndPosition")
    right_end_position = fields.IntField(db_field="rightEndPosition")

    meta = {'abstract': True}


class RegulationPositions(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(db_field="leftEndPosition")
    right_end_position = fields.IntField(db_field="rightEndPosition")

    meta = {'abstract': True}


class Operon(DynamicDocument, BiologicalBase):
    genes = fields.EmbeddedDocumentListField(Genes, required=False)
    regulation_positions = fields.EmbeddedDocumentField(RegulationPositions, required=False, db_field="regulationPositions")
    type = fields.StringField(required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)