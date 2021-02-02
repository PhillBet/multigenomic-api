from ..models.publications import Publications
from . import base


def get_all():
    return base.get_all(Publications)


def find_by_id(id_: str):
    return base.find_one_by_id(Publications, id_)


def find_by_pmid(pmid: str):
    return Publications.objects.get(pmid=pmid)
