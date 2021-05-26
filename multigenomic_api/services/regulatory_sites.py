from ..models.regulatory_sites import RegulatorySites
from . import base


def get_all() -> [RegulatorySites]:
    return base.get_all(RegulatorySites)


def find_by_id(id_: str) -> RegulatorySites:
    return base.find_one_by_id(RegulatorySites, id_)

