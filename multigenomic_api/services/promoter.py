from ..models.promoter import Promoter
from . import base


def get_all() -> [Promoter]:
    return base.get_all(Promoter)


def find_by_id(id_: str) -> Promoter:
    return base.find_one_by_id(Promoter, id_)