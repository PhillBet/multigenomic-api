from ..models.gene import Gene
from . import base


def get_all() -> [Gene]:
    return base.get_all(Gene)


def find_by_id(id_: str) -> Gene:
    return base.find_one_by_id(Gene, id_)


def find_by_bnumber(bnumber: str) -> Gene:
    return Gene.objects(bnumber=bnumber)


def find_by_bnumbers(bnumbers: [str]) -> [Gene]:
    return Gene.objects().filter(bnumber__in=bnumbers)


def get_id_by_bnumbers(bnumbers: [str]) -> [Gene]:
    genes = Gene.objects().filter(bnumber__in=bnumbers).only("id").only("bnumber")
    gene_bnumber = {}
    for gene in genes:
        gene_bnumber[gene.bnumber] = gene.id
    return gene_bnumber


def get_all_gene_product_relationships():
    results = Gene.objects().aggregate(*[{
        '$lookup': {
            'from': "product",
            'localField': '_id',
            'foreignField': 'gene_id',
            'as': 'products'
        }
    }])
    return results


def get_gene_motifs_relationship():
    results = Gene.objects().aggregate(*[{
        '$lookup': {
            'from': "product",
            'localField': '_id',
            'foreignField': 'gene_id',
            'as': 'products'
        }},
        # {"$unwind": "$products"},
        {"$lookup": {
            "from": "motif",
            "localField": "products._id",
            "foreignField": "product_id",
            "as": "motifs"
        }},
        # {"$unwind": "$motifs"},
        {"$project": {"_id": 1, "name": 1, "products._id": 1, "products.name": 1, "motifs._id": 1, "motifs.sequence": 1}},
        {"$count": "passing_scores"}
    ])
    return results

