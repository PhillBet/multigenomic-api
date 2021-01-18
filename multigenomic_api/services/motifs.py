from ..models.motifs import Motifs
from . import base


def get_all() -> [Motifs]:
    return base.get_all(Motifs)


def find_by_id(id_: str) -> Motifs:
    return base.find_one_by_id(Motifs, id_)


def find_by_product_id(products_id: str) -> [Motifs]:
    return Motifs.objects(products_id=products_id)
