from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Сохраняем введенное значение пароля
        if 'password' in self.data:
            self.fields['password'].widget.attrs['value'] = self.data['password']
            
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password1' in self.data:
            self.fields['password1'].widget.attrs['value'] = self.data['password1']
        if 'password2' in self.data:
            self.fields['password2'].widget.attrs['value'] = self.data['password2']