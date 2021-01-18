from ..models.transcription_units import TranscriptionUnits
from . import base


def get_all():
    return base.get_all(TranscriptionUnits)


def find_by_id(id_: str):
    return base.find_one_by_id(TranscriptionUnits, id_)


def find_by_operon_id(operons_id: str) -> [TranscriptionUnits]:
    return TranscriptionUnits.objects(operons_id=operons_id)
