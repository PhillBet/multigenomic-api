from ..models.terms import Terms
from . import base


def get_all() -> [Terms]:
    return base.get_all(Terms)


def find_by_id(id_: str) -> Terms:
    return base.find_one_by_id(Terms, id_)


def get_associated_members_ids(id_: str, member_type) -> [str]:
    members = Terms.objects(_id=id_).only("members").first()
    members_ids = members["members"][member_type]
    return members_ids
