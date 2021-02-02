from ..models.transcription_factor import TranscriptionFactors
from mongoengine.errors import DoesNotExist
from . import base


def get_all() -> [TranscriptionFactors]:
    return base.get_all(TranscriptionFactors)


def find_by_id(id_: str) -> TranscriptionFactors:
    return base.find_one_by_id(TranscriptionFactors, id_)


def find_by_name(name: [str]) -> [TranscriptionFactors]:
    return TranscriptionFactors.objects().filter(name=name)


def find_tf_id_by_product_id(product_id) -> str or None:
    try:
        tf = TranscriptionFactors.objects.get(active_conformations__id=product_id)
        return tf.id
    except DoesNotExist:
        return None

