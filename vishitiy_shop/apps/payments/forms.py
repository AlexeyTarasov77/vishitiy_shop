from django import forms  # Импортируем forms из Django для создания форм
from django.urls import reverse
from .novaposhta import NovaPoshta

np = NovaPoshta()


from django import forms
from django_countries.fields import CountryField


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

    def get_autocomplete_field_attrs(self, url_name):
        return {
            "hx-get": reverse(url_name),
            "hx-trigger": "input changed delay:500ms, search",
            "hx-target": "closest .autocomplete",
            "hx-swap": "beforeend",
            "hx-indicator": "#indicator",
        }

    def __init__(self, *args, **kwargs):
        # Вызывает конструктор родительского класса (forms.Form).
        super().__init__(*args, **kwargs)
        # проходится (переьирает) все поля формы
        self.fields["city"].widget.attrs.update(
            self.get_autocomplete_field_attrs("payments:get-cities")
        )
        self.fields["post_office"].widget.attrs.update(
            {
                **self.get_autocomplete_field_attrs("payments:get-post-offices"),
                "hx-include": "#div_id_city input",
            }
        )
        for field in self.fields:
            # Обновляет атрибуты виджета каждого поля формы
            self.fields[field].widget.attrs.update(
                {"class": "border border-light text-white bg-black form-control"}
            )

    # def clean_post_office(self):
    #     post_office_description = self.cleaned_data["post_office"]
    #     post_office = np.get_post_offices(Description=post_office_description)["data"]
    #     print(post_office)
    #     if not post_office:
    #         raise forms.ValidationError("Виберіть відділення Нової пошти")
    #     elif post_office == []:
    #         raise forms.ValidationError("Такого відділення Нової пошти не існує")
    #     return post_office
