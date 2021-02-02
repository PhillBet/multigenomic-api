from ..models.transcription_factor_regulatory_sites import TranscriptionFactorRegulatorySites
from . import base


def get_all() -> [TranscriptionFactorRegulatorySites]:
    return base.get_all(TranscriptionFactorRegulatorySites)


def find_by_id(id_: str) -> TranscriptionFactorRegulatorySites:
    return base.find_one_by_id(TranscriptionFactorRegulatorySites, id_)

