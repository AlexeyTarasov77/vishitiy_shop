from django import forms
from django.utils.translation import gettext as _

from products.models import Product


class CustomDesignForm(forms.Form):
    # design data
    base_product = forms.ChoiceField(
        label="Базовий продукт", choices=(("Hoodie", _("Hoodie")), ("T-shirt", _("T-shirt")))
    )
    color = forms.ChoiceField(label=_("Колір"), choices=Product.COLOR_CHOICES)
    size = forms.ChoiceField(label=_("Розмір"), choices=Product.SIZE_CHOICES)
    design_type = forms.ChoiceField(
        label="Тип дизайну", choices=(("print", _("Print")), ("embroidery", _("Embroidery")))
    )
    design_image = forms.ImageField(label="Зображення дизайну", required=False)
    # personal data
    phone_number = forms.CharField(label="Номер телефону")
    comment = forms.CharField(widget=forms.Textarea, max_length=100, label=_("Комментар/Побажання"))
