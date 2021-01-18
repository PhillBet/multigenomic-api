from ..models.operons import Operons
from . import base


def get_all() -> [Operons]:
    return base.get_all(Operons)


def find_by_id(id_: str) -> Operons:
    return base.find_one_by_id(Operons, id_)


def find_by_gene_id(gene_id: str) -> Operons:
    operon = Operons.objects.filter(genes__match={"gene_id": gene_id}).first()
    return operon

