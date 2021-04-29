from ..models.promoters import Promoters
from . import base


def get_all() -> [Promoters]:
    return base.get_all(Promoters)


def find_by_id(id_: str) -> Promoters:
    return base.find_one_by_id(Promoters, id_)


def find_by_sigma_factor_id(sigma_factor_id: str) -> Promoters:
    return Promoters.objects(__raw__={"bindsSigmaFactor.sigmaFactors_id": sigma_factor_id})
