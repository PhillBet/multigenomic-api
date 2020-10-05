from ..models.term import Term
from . import base


def get_all() -> [Term]:
    return base.get_all(Term)


def find_by_id(id_: str) -> Term:
    return base.find_one_by_id(Term, id_)


def get_associated_members_ids(id_: str, member_type) -> [str]:
    members = Term.objects(_id=id_).only("members").first()
    members_ids = members["members"][member_type]
    return members_ids
