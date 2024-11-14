from django import forms  # Импорт модуля форм Django
from products.models import Product  # Импорт модели Product

from .cart import Cart  # Импорт класса Cart для работы с корзиной


class CartBaseForm(forms.Form):
    """Базовая форма корзины, не используеться извне.
    Хранит небходимые методы для корректной работы корзины.
    (Обеспечения переданного запроса и провалидированной формы перед сохранением).
    В методе save происходит инициализация корзины и вызов метроды для добавления продукта,
    которому передаются отвалидированные данные.
    """

    def process_request(self, request):
        # Метод для обработки запроса. Устанавливает атрибут request.
        print("CALLING METHOD", request)
        self.request = request

    def save(self):
        # Метод сохранения. Проверяет валидность формы и наличие запроса.
        assert self.is_valid(), "Form is not valid"
        assert self.request, "Request is not provided"


class CartAddForm(CartBaseForm):
    """
    Форма добавления в корзину.
    Содержит дополнительную валидацию того, что добавляемый продукт еще не добавлялся в корзину.
    """

    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(initial=1, min_value=1, required=False)
    size = forms.ChoiceField(choices=Product.SIZE_CHOICES)
    color = forms.ChoiceField(choices=Product.COLOR_CHOICES)
    price = forms.DecimalField()

    def clean(self):
        # Метод очистки данных формы проверяет, что продукт еще не добавлен в корзину.

        if getattr(self, "request", None):
            cart = Cart(self.request)
            if self.cleaned_data["product_id"] in cart:
                raise forms.ValidationError("Продукт вже знаходиться в корзині")
        return self.cleaned_data

    def save(self):
        # Переопределенный метод сохранения. Вызывает базовый метод сохранения и добавляет продукт в корзину.
        super().save()
        self.cleaned_data["price"] = str(
            self.cleaned_data["price"]
        )  # перевод в строку т.к. Decimal не сериализуется
        cart = Cart(self.request)
        return cart.add(**self.cleaned_data)


class CartUpdateForm(CartBaseForm):
    """
    Форма обновления колва товара в корзины.
    """

    product_id = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1)

    def save(self):
        # Переопределенный метод сохранения. Обновляет количество продукта в корзине.
        cart = Cart(self.request)
        return cart.update(**self.cleaned_data)


class CartRemoveForm(CartBaseForm):
    """Форма удаления продукта из корзины."""

    product_id = forms.CharField(widget=forms.HiddenInput)

    def save(self):
        # Переопределенный метод сохранения. Удаляет продукт из корзины.
        cart = Cart(self.request)
        return cart.remove(**self.cleaned_data)
