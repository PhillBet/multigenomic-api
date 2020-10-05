from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .biological_base import BiologicalBase


class Gene(DynamicEmbeddedDocument):
    distance_to = fields.FloatField(required=False, db_field="distanceTo")
    gene_id = fields.StringField(required=True)
    gene_name = fields.StringField(required=False)
    meta = {'abstract': True}


class Promoter(DynamicEmbeddedDocument):
    distance_to = fields.FloatField(required=False, db_field="distanceTo")
    promoter_id = fields.StringField(required=True)
    promoter_name = fields.StringField(required=False)
    meta = {'abstract': True}


class RegulatedEntity(DynamicEmbeddedDocument):
    id = fields.StringField(required=True, db_field="_id")
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class Regulator(DynamicEmbeddedDocument):
    id = fields.StringField(required=True, db_field="_id")
    name = fields.StringField(required=False)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class TranscriptionFactorRegulatorySite(DynamicEmbeddedDocument, BiologicalBase):
    absolute_position = fields.FloatField(required=False, db_field="absolutePosition")
    length = fields.IntField(required=False)
    meta = {'abstract': True}


class RegulatoryInteraction(DynamicDocument, BiologicalBase):
    center_position = fields.FloatField(required=False, db_field="centerPosition")
    gene = fields.EmbeddedDocumentField(Gene, required=False)
    function = fields.StringField(required=False)
    promoters = fields.EmbeddedDocumentListField(Promoter, required=False)
    regulated_entities = fields.EmbeddedDocumentListField(RegulatedEntity, required=True, db_field="regulatedEntities")
    regulator = fields.EmbeddedDocumentField(Regulator, required=True)
    transcription_factor_regulatory_site = fields.EmbeddedDocumentField(TranscriptionFactorRegulatorySite, required=False, db_field="transcriptionFactorRegulatorySite")

    type = fields.StringField(required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulatoryInteraction'}
