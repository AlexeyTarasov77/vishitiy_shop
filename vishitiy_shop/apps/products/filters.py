import django_filters
import django_filters.widgets
from django import forms
from django.db.models import QuerySet

from products.models import Collection, Product
from products.widgets import CustomRangeWidget


class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(
        widget=CustomRangeWidget(
            attrs={"class": "px-3 py-2 border border-gray-200 rounded w-24 text-center"}
        ),
        label="Ціна",
    )

    size = django_filters.TypedMultipleChoiceFilter(
        field_name="available_sizes",
        choices=Product.SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="icontains",
        label="Розмір",
    )

    collection = django_filters.ModelMultipleChoiceFilter(
        queryset=Collection.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Колекція",
    )

    color = django_filters.TypedMultipleChoiceFilter(
        field_name="available_colors",
        choices=Product.COLOR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        lookup_expr="icontains",
        label="Колір",
    )

    discounted_only = django_filters.BooleanFilter(
        field_name="discount",
        label="Тiльки зi знижкою",
        widget=forms.CheckboxInput,
        method="filter_discounted_only",
    )

    def filter_discounted_only(self, queryset: QuerySet, name, value) -> QuerySet:
        if value:
            return queryset.filter(discount__gt=0)
        return queryset

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
