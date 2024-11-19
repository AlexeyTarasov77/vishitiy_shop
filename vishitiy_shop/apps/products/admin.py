from django.contrib import admin

from products.models import Collection, Product
from products.widgets import ArrayCheckboxWidget

admin.site.register(Collection)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "final_price", "collection", "available"]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["available_sizes"].widget = ArrayCheckboxWidget(
            choices=Product.SIZE_CHOICES,
            attrs={"class": "form-control"},
        )

        form.base_fields["available_colors"].widget = ArrayCheckboxWidget(
            choices=Product.COLOR_CHOICES,
            attrs={"class": "form-control"},
        )

        # Возвращаем кастомизированную форму
        return form
