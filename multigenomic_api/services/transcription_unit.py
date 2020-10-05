from ..models.transcription_unit import TranscriptionUnit
from . import base


def get_all():
    return base.get_all(TranscriptionUnit)


def find_by_id(id_: str):
    return base.find_one_by_id(TranscriptionUnit, id_)


def find_by_operon_id(operon_id: str) -> [TranscriptionUnit]:
    return TranscriptionUnit.objects(operon_id=operon_id)
