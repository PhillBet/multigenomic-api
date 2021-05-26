from ..models.terminators import Terminators
from . import base


def get_all():
    return base.get_all(Terminators)


def find_by_id(id_: str):
    return base.find_one_by_id(Terminators, id_)



