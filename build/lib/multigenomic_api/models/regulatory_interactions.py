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
    name = fields.StringField(required=True)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class Regulator(DynamicEmbeddedDocument):
    id = fields.StringField(required=True, db_field="_id")
    name = fields.StringField(required=False)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class RegulatoryInteractions(DynamicDocument, BiologicalBase):
    center_position = fields.FloatField(required=False, db_field="centerPosition")
    function = fields.StringField(required=False)
    mechanism = fields.StringField(required=False)
    regulated_entity = fields.EmbeddedDocumentField(RegulatedEntity, required=True, db_field="regulatedEntity")
    regulator = fields.EmbeddedDocumentField(Regulator, required=True)
    regulatory_sites_id = fields.StringField(required=False, db_field="regulatorySites_id")
    type = fields.StringField(required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    meta = {'collection': 'regulatoryInteractions'}
