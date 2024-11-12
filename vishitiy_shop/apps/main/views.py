import logging
import os
import smtplib
from itertools import zip_longest

from django import http
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from products.models import Collection, Product

from main import forms


@require_http_methods(["GET"])
def index_view(request: http.HttpRequest) -> http.HttpResponse:
    discounted_products = Product.objects.filter(discount__gte=20)
    grouped_discounted_products = zip_longest(
        *[iter(discounted_products)] * 4, fillvalue=None
    )
    context = {
        "collections": Collection.objects.all(),
        "grouped_products": grouped_discounted_products,
    }
    return render(request, "main/index.html", context)


@require_http_methods(["GET"])
def get_algolia_credentials_view(request: http.HttpRequest) -> http.JsonResponse:
    return http.JsonResponse(
        {
            "APP_ID": os.getenv("ALGOLIA_APP_ID"),
            "API_KEY": os.getenv("ALGOLIA_API_KEY"),
        }
    )


@require_http_methods(["GET"])
def about_us_view(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "main/about_us.html")


@require_http_methods(["GET", "POST"])
def contacts_view(request: http.HttpRequest) -> http.HttpResponse:
    form = forms.ContactForm(request.POST or None)
    if request.method == "POST":
        if not form.is_valid():
            print("Invalid form", form.errors)
            return render(request, "main/contacts.html", {"form": form})

        data = form.cleaned_data

        email_msg_body = f"""
            Ім'я: {data["name"]}
            Номер телефону: {data["phone_number"]}
            Email: {data["email"]}
            Повідомлення: {data["message"]}
        """
        try:
            send_mail(
                "Контакт користувача",
                email_msg_body,
                data["email"],
                [settings.EMAIL_HOST_USER],
            )
        except smtplib.SMTPException as e:
            logging.exception(e)
            messages.error(request, "Помилка при відправленні повідомлення")
        else:
            messages.success(request, "Ваше повідомлення успішно відправлено")
    return render(request, "main/contacts.html", {"form": form})
