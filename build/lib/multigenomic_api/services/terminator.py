from ..models.terminator import Terminator
from . import base


def get_all():
    return base.get_all(Terminator)


def find_by_id(id_: str):
    return base.find_one_by_id(Terminator, id_)



