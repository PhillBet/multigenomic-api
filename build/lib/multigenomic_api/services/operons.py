from ..models.operons import Operons
from ..services import transcription_units
from . import base


def get_all() -> [Operons]:
    return base.get_all(Operons)


def find_by_id(id_: str) -> Operons:
    return base.find_one_by_id(Operons, id_)


def find_by_gene_id(gene_id: str) -> Operons:
    operon_id = transcription_units.get_operons_id_by_gene_id(gene_id)
    if operon_id:
        return find_by_id(operon_id)
    return None

