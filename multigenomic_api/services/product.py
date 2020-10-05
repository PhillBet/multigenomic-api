from ..models.product import Product
from . import base


def get_all() -> [Product]:
    return base.get_all(Product)


def find_by_id(id_: str) -> Product:
    return base.find_one_by_id(Product, id_)


def find_by_gene_id(gene_id: str) -> Product:
    return Product.objects(gene_id=gene_id)
