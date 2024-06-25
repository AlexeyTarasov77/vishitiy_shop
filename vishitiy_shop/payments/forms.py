from django import forms  # Импортируем forms из Django для создания форм
from django_countries import countries  # Импортируем список стран из django-countries
from django_countries.fields import CountryField  # Импортируем поле страны из django-countries
from novaposhta_api.models import NP_City, NP_WareHouse
import requests

def get_cities_choices():
    api_url = 'https://api.novaposhta.ua/v2.0/json/'
    api_key = 'd163f31ac2f2738242a3c3d2875c8020'

    # Получение списка городов
    cities_response = requests.post(api_url, json={
        'apiKey': api_key,
        'modelName': 'Address',
        'calledMethod': 'getCities',
        'methodProperties': {}
    })
    cities_data = cities_response.json()['data']
    # print(cities_data)
    return [(city['Ref'], city['Description']) for city in cities_data]
    

class PaymentForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефону')  # поле для ввода номера телефона
    email = forms.EmailField(label='Email')  # поле для ввода email
    name = forms.CharField(label='Ім`я')  # поле для ввода имени
    country = CountryField().formfield(label="Країна")  # поле для выбора страны используя библиотеку django-countries )))
    post = forms.CharField(label='Поштовий індекс')  # Поле для ввода почтового индекса
    cities = forms.ModelChoiceField(label='Місто', queryset=NP_City.objects.all(), empty_label='Виберіть місто')
    # post_offices = forms.ModelChoiceField(label='Поштомат', queryset=NP_WareHouse.objects.filter(Type__Description='Поштомат'), empty_label='Виберіть поштовий офіс')
    
    # конструктор класса PaymentForm
    def __init__(self, *args, **kwargs):
        # Вызывает конструктор родительского класса (forms.Form).
        super().__init__(*args, **kwargs)
        # проходится (переьирает) все поля формы
        for field in self.fields:
            # Обновляет атрибуты виджета каждого поля формы
            self.fields[field].widget.attrs.update({'class': 'border border-light text-white bg-black'})
            


