from django.conf import (
    settings,
)  # Импорт настроек Django для доступа к ключу сессии корзины
from products.models import Product  # Импорт модели Product для доступа к товарам
from decimal import Decimal  # Импорт Decimal для работы с десятичными числами


class Cart:
    """
    Класс для управления корзиной (добавление, удаление, обновление)
    Так же содержатся dunder методы для итерации и провеки вхождения с помощью оператора in.
    На вход методы ожидают полностью провалидированные данные от формы.
    """

    def __init__(self, request):
        # Инициализация корзины на основе сессии пользователя
        self.session = request.session
        # Получение существующей корзины из сессии или создание новой, если она не существует
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        # Получение всех товаров из базы данных, соответствующих идентификаторам в корзине
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            # Добавление информации о товаре в корзине
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            # Преобразование цены товара в десятичное число и вычисление общей стоимости
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        print('calling len')
        return sum([item["quantity"] for item in self.cart.values()])


    def contains_deep(self, product_id, **params):
        # Проверяет содержит ли корзина товар с указанными параметрами глубоко
        if params:
            for key, value in params.items():
                if self.cart[product_id][key] != value:
                    return False
        return True

    def __contains__(self, product_id):
        return str(product_id) in self.cart

    def add(self, **data) -> dict | None:
        # Добавляет товар в корзину
        product_id = data.pop("product_id")
        assert product_id not in self.cart, "Product already in cart"
        self.cart[product_id] = data
        self.save()
        return self._get_response_data(self.cart[product_id])

    def save(self):
        # Сохраняет изменения в корзине в сессии
        self.session.modified = True

    def remove(self, product_id):
        assert product_id in self.cart, "Product not in cart"
        del self.cart[product_id]
        self.save()
        return self._get_response_data()

    def update(self, **data):
        # Обновляет информацию о товаре в корзине
        product_id = data.pop("product_id")
        assert product_id in self.cart, "Product not in cart"
        self.cart[product_id].update(**data)
        self.save()
        return self._get_response_data(self.cart[product_id])

    def clear(self):
        # Очищает корзину пользователя
        del self.session[settings.CART_SESSION_KEY]
        self.save()

    def _get_response_data(self, item=None):
        return {"item": item, "total": self.get_total(), "len": sum([item["quantity"] for item in self.cart.values()])}

    def get_total(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

