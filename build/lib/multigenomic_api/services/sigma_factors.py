from ..models.sigma_factors import SigmaFactors
from mongoengine.errors import DoesNotExist
from . import base


def get_all() -> [SigmaFactors]:
    return base.get_all(SigmaFactors)


def find_by_id(id_: str) -> SigmaFactors:
    return base.find_one_by_id(SigmaFactors, id_)


def find_by_gene_id(gene_id: str) -> SigmaFactors:
    try:
        return SigmaFactors.objects.get(genes_id=gene_id)
    except DoesNotExist:
        return None
