from ..models.external_cross_reference import ExternalCrossReference
from . import base


def get_all():
    return base.get_all(ExternalCrossReference)


def find_by_id(id_: str):
    return base.find_one_by_id(ExternalCrossReference, id_)


