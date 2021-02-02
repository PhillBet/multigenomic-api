from ..models.organisms import Organisms
from . import base


def get_all() -> [Organisms]:
    return base.get_all(Organisms)


def find_by_id(id_: str) -> Organisms:
    return Organisms.objects.filter(_id=id_).first()