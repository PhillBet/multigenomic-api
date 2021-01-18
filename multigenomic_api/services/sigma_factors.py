from ..models.sigma_factors import SigmaFactors
from . import base


def get_all() -> [SigmaFactors]:
    return base.get_all(SigmaFactors)


def find_by_id(id_: str) -> SigmaFactors:
    return base.find_one_by_id(SigmaFactors, id_)
