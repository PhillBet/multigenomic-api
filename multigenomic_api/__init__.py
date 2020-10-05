import mongoengine

from .services import evidence
from .services import external_cross_reference
from .services import gene
from .services import motif
from .services import operon
from .services import organism
from .services import product
from .services import promoter
from .services import publication
from .services import regulatory_complex
from .services import regulatory_continuant
from .services import regulatory_interaction
from .services import sigma_factor
from .services import term
from .services import terminator
from .services import transcription_unit


def connect(database, uri):
    mongoengine.connect(database, host=uri)


def disconnect():
    mongoengine.disconnect()

