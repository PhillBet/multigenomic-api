from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .base import Base


class TranscriptionTerminationSite(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    range = fields.StringField(required=False)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class Terminator(DynamicDocument, Base):

    class_ = fields.StringField(required=False, db_field="class")
    transcriptionTerminationSite = fields.EmbeddedDocumentField(TranscriptionTerminationSite, required=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
