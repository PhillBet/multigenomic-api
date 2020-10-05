from ..models.motif import Motif
from . import base


def get_all() -> [Motif]:
    return base.get_all(Motif)


def find_by_id(id_: str) -> Motif:
    return base.find_one_by_id(Motif, id_)


def find_by_product_id(product_id: str) -> [Motif]:
    return Motif.objects(product_id=product_id)
