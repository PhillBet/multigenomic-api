from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument


from .biological_base import BiologicalBase
from .biological_base import Citations


class BindsSigmaFactor(DynamicEmbeddedDocument):
    citations = fields.EmbeddedDocumentListField(Citations, required=False, db_field="citations")

    meta = {'abstract': True}


class MinusSignals(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    sequence = fields.StringField(required=False)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class PromoterFeatures(DynamicEmbeddedDocument, BiologicalBase):
    promoter_feature_id = fields.StringField(required=True, db_field="promoterFeature_id")
    binds_sigma_factor = fields.EmbeddedDocumentField(BindsSigmaFactor, required=False, db_field="bindsSigmaFactor")
    minus_signals = fields.EmbeddedDocumentListField(MinusSignals, required=False, db_field="minusSignals")
    score = fields.FloatField(required=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    meta = {'abstract': True}


class TranscriptionStartSite(DynamicEmbeddedDocument):
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    range = fields.StringField(required=False)
    type = fields.StringField(required=False)
    meta = {'abstract': True}


class Promoter(DynamicDocument, BiologicalBase):

    pos1 = fields.IntField(required=False)
    promoter_features = fields.EmbeddedDocumentListField(PromoterFeatures, required=False, db_field="promoterFeatures")
    sigma_factor_id = fields.StringField(required=False, db_field="sigmaFactor_id")
    transcription_start_site = fields.EmbeddedDocumentField(TranscriptionStartSite, required=False, db_field="transcriptionStartSite")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
