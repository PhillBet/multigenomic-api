from mongoengine import fields
from mongoengine import EmbeddedDocument

from .base import Base


class TermParent:
    terms_id = fields.StringField(required=False)
    terms_name = fields.StringField(required=False)


class Citations(EmbeddedDocument):
    publications_id = fields.StringField(required=False)
    evidences_id = fields.StringField(required=False)


class ExternalCrossReferences(EmbeddedDocument):
    external_cross_references_id = fields.StringField(required=False, db_field="externalCrossReferences_id")
    object_id = fields.StringField(required=False, db_field="objectId")


class BiologicalBase(Base):
    citations = fields.EmbeddedDocumentListField(Citations, db_field="citations")
    external_cross_references = fields.EmbeddedDocumentListField(ExternalCrossReferences, db_field="externalCrossReferences")
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    organisms_id = fields.StringField(required=False)
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    sequence = fields.StringField(required=False)
    strand = fields.StringField(required=False)
    synonyms = fields.ListField(required=False)

    def __init__(self, **kwargs):
        super().__init__()
