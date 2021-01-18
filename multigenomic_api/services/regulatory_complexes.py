from ..models.regulatory_complexes import RegulatoryComplexes
from . import base


def get_all() -> [RegulatoryComplexes]:
    return base.get_all(RegulatoryComplexes)


def find_by_id(id_: str) -> RegulatoryComplexes:
    return base.find_one_by_id(RegulatoryComplexes, id_)
