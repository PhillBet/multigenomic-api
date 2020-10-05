from ..models.regulatory_continuant import RegulatoryContinuant
from . import base


def get_all() -> [RegulatoryContinuant]:
    return base.get_all(RegulatoryContinuant)


def find_by_id(id_: str) -> RegulatoryContinuant:
    return base.find_one_by_id(RegulatoryContinuant, id_)
