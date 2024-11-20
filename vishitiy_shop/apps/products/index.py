from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product


@register(Product)
# Регистрируем модель Product для индексации в Algolia
class ProductIndex(AlgoliaIndex):
    fields = ("title", "category", "url", "image_url", "price")
    index_name = "products"
    settings = {
        "searchableAttributes": ["title"],
        "attributesForFaceting": [
            "color",
            "size",
            "category",
        ],
    }
