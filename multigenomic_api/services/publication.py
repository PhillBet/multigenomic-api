from ..models.publication import Publication
from . import base


def get_all():
    return base.get_all(Publication)


def find_by_id(id_: str):
    return base.find_one_by_id(Publication, id_)


def find_by_pmid(pmid: str):
    return Publication.objects.get(pmid=pmid)
