from ..models.evidence import Evidence
from . import base


def get_all():
    return base.get_all(Evidence)


def find_by_id(id_: str):
    return base.find_one_by_id(Evidence, id_)


