import json

import requests
from cart.cart import Cart
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from payments.novaposhta import NovaPoshta

from . import forms


def get_post_offices_view(request):
    np = NovaPoshta()
    print(request.GET)
    post_office = request.GET.get("post_office")
    city = request.GET.get("city")
    post_offices = []
    if post_office and city:
        post_offices = np.get_post_offices(CityName=city, FindByString=post_office)["data"][:10]
    return render(request, "payments/partials/post_offices.html", {"post_offices": post_offices})


def get_cities_view(request):
    np = NovaPoshta()
    print(request.GET)
    city = request.GET.get("city")
    cities = []
    if city:
        cities = np.search_cities(CityName=city)["data"][0]["Addresses"]
    print(cities)
    return render(request, "payments/partials/cities.html", {"cities": cities})


def payment_view(request):
    if request.method == "POST":
        print("INTO POST")
        form = forms.PaymentForm(request.POST)  # Создаем форму PaymentForm из POST-запроса
        cart = Cart(request)  # Создаем объект корзины
        if not cart:
            return HttpResponse("Корзина пуста", status=400)
        basket_order = []
        for item in cart:
            basket_order.append({
                "name": item["product"].title,
                "qty": item["quantity"],
                "sum": int(item["total_price"] * 100),
                "icon": request.build_absolute_uri(item["product"].image.url),
                "unit": "шт.",
                "code": item["product"].slug,
                "barcode": "string",
                "header": "string",
                "footer": "string",
                "tax": [],
            })
        data = {
            "amount": int(cart.get_total() * 100),
            "merchantPaymInfo": {
                "destination": "Оплата замовлення",
                "basketOrder": basket_order,
            },
            "redirectUrl": request.build_absolute_uri(reverse("payments:payment-status")),
            "webHookUrl": request.build_absolute_uri(reverse("payments:monobank-webhook")),
        }
        headers = {"X-Token": settings.MONOBANK_API_TOKEN, "Content-Type": "application/json"}
        resp = requests.post(
            "https://api.monobank.ua/api/merchant/invoice/create", json=data, headers=headers
        )
        if resp.status_code == 200:
            if form.is_valid():  # Проверяем валидность формы
                cd = form.cleaned_data  # Получаем очищенные данные из формы
                cd["phone_number"] = request.POST.get("tel")
                cart = Cart(request)  # Создаем объект корзины
                context = {
                    "data": cd,
                    "cart": cart,
                    "user": request.user,
                }  # Формируем контекст для шаблона

                # Генерируем HTML-контент на основе шаблона 'payments/order_info.html' и контекста
                html_content = render_to_string("payments/order_info.html", context)
                plain_message = strip_tags(
                    html_content
                )  # Создаем обычное текстовое сообщение без HTML-тегов

                # Выводим содержимое html_content и plain_message в консоль для отладки
                print(html_content, plain_message, sep="\n")
                print("BEFORE SENDING REQUEST")
                # Отправляем письмо
                send_mail(
                    "YOUR ORDER",  # Название сообщения
                    plain_message,  # Текст сообщения без HTML
                    settings.EMAIL_HOST_USER,  # кто будет отправлять
                    [cd["email"]],  # получатель сообщения
                    fail_silently=False,
                    html_message=html_content,  # ХТМЛ содержимое письма
                )
                return redirect(resp.json()["pageUrl"])
            print(form.errors)
            return render(request, "payments/email_form.html", {"form": form})
        
        return JsonResponse(resp.json(), status=resp.status_code)

    form = forms.PaymentForm()  # Если метод запроса GET создаем пустую форму PaymentForm
    return render(
        request,
        "payments/email_form.html",
        {"form": form},
    )  # Выводим форму на страницу email_form.html


@csrf_exempt
def monobank_webhook(request):
    print('WEBHOOOOOK')
    payload = json.loads(request.body)
    print("WEBHOOK PAYLOAD: ", payload)
    if payload.get("status") == "success":
        return HttpResponse(status=200)


def payment_status_view(request):
    cart = Cart(request)
    if cart:
        cart.clear()
    return render(request, "payments/payment_status.html")