def get_all(model):
    return model.objects


def find_one_by_id(model, object_id=str):
    return model.objects.get(_id=object_id)