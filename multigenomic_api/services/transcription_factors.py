from ..models.transcription_factor import TranscriptionFactors
from . import base


def get_all() -> [TranscriptionFactors]:
    return base.get_all(TranscriptionFactors)


def find_by_id(id_: str) -> TranscriptionFactors:
    return base.find_one_by_id(TranscriptionFactors, id_)


def find_by_name(name: [str]) -> [TranscriptionFactors]:
    return TranscriptionFactors.objects().filter(name=name)
