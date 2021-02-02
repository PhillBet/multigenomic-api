from ..models.external_cross_references import ExternalCrossReferences
from . import base


def get_all():
    return base.get_all(ExternalCrossReferences)


def find_by_id(id_: str):
    return base.find_one_by_id(ExternalCrossReferences, id_)


