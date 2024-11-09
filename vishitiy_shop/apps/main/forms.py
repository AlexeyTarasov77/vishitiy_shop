from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Ім`я")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Повідомлення")
    phone_number = forms.CharField(label="Номер телефону")

    def clean_phone_number(self) -> str:
        country_code = "+380"
        phone_number: str = self.cleaned_data["phone_number"]
        required_len = 9
        if len(phone_number) != required_len:
            raise forms.ValidationError(
                f"Номер телефону повинен містити {required_len} цифр"
            )
        for char in phone_number:
            if not char.isdigit():
                raise forms.ValidationError("Номер телефону повинен містити тільки цифри.")
        return country_code + phone_number
