from ..models.regulatory_interaction import RegulatoryInteraction
from . import base


def get_all() -> [RegulatoryInteraction]:
    return base.get_all(RegulatoryInteraction)


def find_by_id(id_: str) -> RegulatoryInteraction:
    return base.find_one_by_id(RegulatoryInteraction, id_)


def find_by_regulated_entity_ids(regulated_entity_ids: [str]) -> [RegulatoryInteraction]:
    regulatery_interactions = []
    for regulated_entity_id in regulated_entity_ids:
        regulatery_interactions.append(RegulatoryInteraction.objects.filter(regulatedEntities__match={"_id": regulated_entity_id}))
    return regulatery_interactions


def find_regulator_by_regulated_entity_id(regulated_entity_id: str) -> [RegulatoryInteraction.regulator]:
    regulators = RegulatoryInteraction.objects().filter(regulatedEntities__match={"_id": regulated_entity_id}).distinct("regulator")
    for regulator in regulators:
        regulator["id"] = regulator.id
    return regulators


def find_regulators_by_regulated_entity_ids(regulated_entity_ids: [str]) -> [RegulatoryInteraction.regulator]:
    regulated_entities_regulators = []
    for regulated_entity_id in regulated_entity_ids:
        regulatory_interactions = RegulatoryInteraction.objects.filter(regulatedEntities__match={"_id": regulated_entity_id})
        for ri in regulatory_interactions:
            if ri.regulator:
                ri.regulator["function"] = ri.function
                if ri.regulator not in regulated_entities_regulators:
                    regulated_entities_regulators.append(ri.regulator)
    return regulated_entities_regulators
