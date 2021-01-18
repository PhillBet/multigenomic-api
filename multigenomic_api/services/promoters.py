from ..models.promoters import Promoters
from . import base


def get_all() -> [Promoters]:
    return base.get_all(Promoters)


def find_by_id(id_: str) -> Promoters:
    return base.find_one_by_id(Promoters, id_)