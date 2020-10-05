from ..models.operon import Operon
from . import base


def get_all() -> [Operon]:
    return base.get_all(Operon)


def find_by_id(id_: str) -> Operon:
    return base.find_one_by_id(Operon, id_)


def find_by_gene_id(gene_id: str) -> Operon:
    operon = Operon.objects.filter(genes__match={"gene_id": gene_id}).first()
    return operon

