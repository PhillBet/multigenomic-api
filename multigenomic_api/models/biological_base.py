from mongoengine import fields
from mongoengine import EmbeddedDocument

from .base import Base
from .evidence import Evidence
from .external_cross_reference import ExternalCrossReference
from .publication import Publication
from .term import Term


class TermParent:
    term_id = fields.StringField(required=False)
    term_name = fields.StringField(required=False)


class Citations(EmbeddedDocument):
    publication_id = fields.StringField(required=False)
    evidence_id = fields.StringField(required=False)


class ExternalCrossReferences(EmbeddedDocument):
    external_cross_reference_id = fields.StringField(required=False, db_field="externalCrossReference_id")
    object_id = fields.StringField(required=False, db_field="objectId")


class CitationDetailed:
    def __init__(self, evidence, publication):
        self.evidence = evidence
        self.publication = publication


class ExternalCrossReferenceDetailed:
    def __init__(self, object_id=None, external_cross_reference=None):
        self.external_cross_reference = external_cross_reference
        self.object_id = object_id


class TermDetailed:
    def __init__(self, term_id):
        self.term = term_id

    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, term_id):
        self._term = Term.objects.get(_id=term_id)


class BiologicalBase(Base):
    citations = fields.EmbeddedDocumentListField(Citations, db_field="citations")
    external_cross_references = fields.EmbeddedDocumentListField(ExternalCrossReferences, db_field="externalCrossReferences")
    left_end_position = fields.IntField(required=False, db_field="leftEndPosition")
    organism_id = fields.StringField(required=False)
    right_end_position = fields.IntField(required=False, db_field="rightEndPosition")
    sequence = fields.StringField(required=False)
    strand = fields.StringField(required=False)
    synonyms = fields.ListField(required=False)

    def __init__(self, **kwargs):
        super().__init__()
        self.citations_detailed = BiologicalBase.citations(kwargs.get("citations", []))
        self.external_cross_references_detailed = BiologicalBase.external_cross_references_detailed(kwargs.get("external_cross_references", []))

    @staticmethod
    def citations_detailed(citations):
        citation_detailed = []
        for citation in citations:
            if citation.evidence_id:
                evidence = Evidence.objects.get(_id=citation.evidence_id)
            else:
                evidence = None
            if citation.publication_id:
                publication = Publication.objects.get(_id=citation.publication_id)
            else:
                publication = None
            citation_detailed.append(CitationDetailed(evidence, publication))
        return citation_detailed

    @staticmethod
    def external_cross_references_detailed(external_cross_references):
        ext_cross_references = []
        for external_cross_reference in external_cross_references:
            if external_cross_reference.external_cross_reference_id:
                external_cross_reference_object = ExternalCrossReference.objects.get(_id=external_cross_reference.external_cross_reference_id)
            else:
                external_cross_reference_object = None
            ext_cross_references.append(ExternalCrossReferenceDetailed(external_cross_reference.object_id, external_cross_reference_object))
        return ext_cross_references
