from ..models.regulatory_complex import RegulatoryComplex
from . import base


def get_all() -> [RegulatoryComplex]:
    return base.get_all(RegulatoryComplex)


def find_by_id(id_: str) -> RegulatoryComplex:
    return base.find_one_by_id(RegulatoryComplex, id_)
