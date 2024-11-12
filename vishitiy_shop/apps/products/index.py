from algoliasearch_django import AlgoliaIndex

# Импортируем класс AlgoliaIndex из пакета algoliasearch_django
from algoliasearch_django.decorators import register


from .models import Product


@register(Product)
# Регистрируем модель Product для индексации в Algolia
class ProductIndex(AlgoliaIndex):
    # Определяем класс ProductIndex, который наследует от AlgoliaIndex
    fields = ("title", "type", "url", "image_url", "price")
    # Поля модели Product, которые будут индексироваться в Algolia
    index_name = "products"
    # Имя индекса в Algolia
    settings = {  # Настройки индекса
        "searchableAttributes": [
            "title"
        ],  # Поля, которые будут использоваться для поиска
        "attributesForFaceting": [
            "color",
            "size",
            "type",
        ],  # Поля, которые будут использоваться для фильтрации
    }
