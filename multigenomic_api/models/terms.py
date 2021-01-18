from mongoengine import fields
from mongoengine import DynamicDocument
from mongoengine import DynamicEmbeddedDocument

from .base import Base


class Members(DynamicEmbeddedDocument):
    genes = fields.ListField(fields.StringField(), required=False)
    products = fields.ListField(fields.StringField(), required=False)
    meta = {'abstract': True}


class CreatedBy(DynamicEmbeddedDocument):
    text = fields.StringField(required=False)
    creation_date = fields.StringField(required=False, db_field="creationDate")

    meta = {'abstract': True}


class Definition(DynamicEmbeddedDocument):
    text = fields.StringField(required=False)
    source = fields.StringField(required=False)

    meta = {'abstract': True}


class Terms(DynamicDocument, Base):
    created_by = fields.EmbeddedDocumentField(CreatedBy, required=False, db_field="createdBy")
    definition = fields.EmbeddedDocumentField(Definition, required=False)
    description = fields.StringField(required=False)
    has_db_x_ref = fields.ListField(fields.StringField(), required=False, db_field="hasDbXRef")
    has_obo_namespace = fields.StringField(required=False, db_field="hasOboNamespace")
    has_related_synonyms = fields.ListField(fields.StringField(), required=False, db_field="hasRelatedSynonyms")
    iri = fields.StringField(required=False)
    members = fields.EmbeddedDocumentField(Members, required=False)
    obo_id = fields.StringField(required=False, db_field="oboId")
    ontologies_id = fields.StringField(required=True)
    sub_class_of = fields.ListField(fields.StringField(), required=False, db_field="subClassOf")
    super_class_of = fields.ListField(fields.StringField(), required=False, db_field="superClassOf")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
