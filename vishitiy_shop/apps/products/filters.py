import django_filters  # Импортируем библиотеку django_filters для создания фильтров
import django_filters.widgets  # Импортируем виджеты из библиотеки django_filters
from django import forms  # Импортируем формы из Django

from .models import Collection, Product  # Импортируем модели Product и Collection
from .widgets import CustomRangeWidget  # Импортируем кастомный виджет для диапазона цен


# Определяем класс фильтра для модели Product
class ProductFilter(django_filters.FilterSet):
    # Фильтр для цены с использованием кастомного виджета диапазона цен
    price = django_filters.RangeFilter(
        widget=CustomRangeWidget(
            attrs={"class": "px-3 py-2 border border-gray-200 rounded w-24 text-center"}
        ),
        label="Ціна",
    )

    # Фильтр для размера с использованием виджета множественного выбора с чекбоксами
    size = django_filters.TypedMultipleChoiceFilter(
        field_name="available_sizes",  # Поле модели, по которому будет фильтрация
        choices=Product.SIZE_CHOICES,  # Доступные варианты размеров
        widget=forms.CheckboxSelectMultiple,  # Виджет для отображения вариантов в виде чекбоксов
        lookup_expr="icontains",  # Метод поиска (независимый от регистра поиск в строках)
        label="Розмір",  # Метка для фильтра
    )

    # Фильтр для коллекции с использованием виджета множественного выбора с чекбоксами
    collection = django_filters.ModelMultipleChoiceFilter(
        queryset=Collection.objects.all(),  # Все объекты коллекции
        widget=forms.CheckboxSelectMultiple,  # Виджет для отображения вариантов в виде чекбоксов
        label="Колекція",  # Метка для фильтра
    )

    # Фильтр для цвета с использованием виджета множественного выбора с чекбоксами
    color = django_filters.TypedMultipleChoiceFilter(
        field_name="available_colors",  # Поле модели, по которому будет фильтрация
        choices=Product.COLOR_CHOICES,  # Доступные варианты цветов
        widget=forms.CheckboxSelectMultiple,  # Виджет для отображения вариантов в виде чекбоксов
        lookup_expr="icontains",  # Метод поиска (независимый от регистра поиск в строках)
        label="Колір",  # Метка для фильтра
    )

    # Фильтр для отображения только товаров со скидкой
    discounted_only = django_filters.BooleanFilter(
        field_name="discount",  # Поле модели, по которому будет фильтрация
        label="Тiльки зi знижкою",  # Метка для фильтра
        widget=forms.CheckboxInput,  # Виджет для отображения в виде чекбокса
        method="filter_discounted_only",  # Метод фильтрации
    )

    def filter_discounted_only(self, queryset, name, value):
        if value:  # Если чекбокс выбран
            return queryset.filter(discount__gt=0)  # Возвращаем товары с ненулевой скидкой
        return queryset  # Иначе возвращаем все товары

    class Meta:
        model = Product
        fields = [
            "price",
            "discounted_only",
            "category",
            "size",
            "color",
            "collection",
        ]
