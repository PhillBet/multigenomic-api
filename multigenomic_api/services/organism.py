from ..models.organism import Organism
from . import base


def get_all() -> [Organism]:
    return base.get_all(Organism)


def find_by_id(id_: str) -> Organism:
    return Organism.objects.filter(_id=id_).first()