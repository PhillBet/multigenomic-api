def get_all(model):
    return model.objects.timeout(False)


def find_one_by_id(model, object_id: str):
    return model.objects.get(_id=object_id)