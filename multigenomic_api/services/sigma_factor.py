from ..models.sigma_factor import SigmaFactor
from . import base


def get_all() -> [SigmaFactor]:
    return base.get_all(SigmaFactor)


def find_by_id(id_: str) -> SigmaFactor:
    return base.find_one_by_id(SigmaFactor, id_)
