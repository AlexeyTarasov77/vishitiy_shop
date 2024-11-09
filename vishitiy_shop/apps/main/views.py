import os
from itertools import zip_longest

from django import http
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from products.models import Collection, Product


def index_view(request: http.HttpRequest) -> http.HttpResponse:
    discounted_products = Product.objects.filter(discount__gte=20)
    grouped_discounted_products = zip_longest(*[iter(discounted_products)] * 4, fillvalue=None)
    context = {
        "collections": Collection.objects.all(),
        "grouped_products": grouped_discounted_products,
    }
    return render(request, "main/index.html", context)


def get_algolia_credentials(request: http.HttpRequest) -> http.JsonResponse:
    return http.JsonResponse({
        "APP_ID": os.getenv("ALGOLIA_APP_ID"),
        "API_KEY": os.getenv("ALGOLIA_API_KEY"),
    })


def about_us(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "main/about_us.html")


def contacts(request: http.HttpRequest) -> http.HttpResponse:
    if request.method == "POST":
        name = request.POST["name"]
        phone_number = request.POST["phone_number"]
        email = request.POST["email"]
        comment = request.POST["comment"]

        message_body = f"""
        Ім'я: {name}
        Номер телефону: {phone_number}
        Email: {email}
        Коментар: {comment}
        """

        # Отправка письма
        send_mail(
            "Контакт користувача",  # Тема письма
            message_body,  # Тело письма
            settings.EMAIL_HOST_USER,  # Отправитель
            ["danilgubarev9804@gmail.com"],  # Получатель
            fail_silently=False,
        )
    return render(request, "main/contacts.html")
