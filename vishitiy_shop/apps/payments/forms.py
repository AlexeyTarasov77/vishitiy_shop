from django import forms
from django.urls import reverse


class PaymentForm(forms.Form):
    email = forms.EmailField(label="Email")  # поле для ввода email
    name = forms.CharField(label="Ім`я")  # поле для ввода имени

    country = forms.CharField(label="Країна")  # Изменено на CharField
    post = forms.CharField(label="Поштовий індекс")  # Поле для ввода почтового индекса
    city = forms.CharField(
        label="Назва або Індекс населеного пункту",
    )
    post_office = forms.CharField(
        label="Відділення Нової пошти",
    )

    def _get_autocomplete_field_attrs(self, url_name: str) -> dict[str, str]:
        return {
            "hx-get": reverse(url_name),
            "hx-trigger": "input changed delay:500ms, search",
            "hx-target": "closest .autocomplete",
            "hx-swap": "beforeend",
            "hx-indicator": "#indicator",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].widget.attrs.update(
            self._get_autocomplete_field_attrs("payments:get-cities")
        )
        self.fields["post_office"].widget.attrs.update({
            **self._get_autocomplete_field_attrs("payments:get-post-offices"),
            "hx-include": "#div_id_city input",
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class": "border border-light text-white bg-black form-control"
            })
