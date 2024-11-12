from django.shortcuts import render
import os
from django.templatetags.static import static
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib.staticfiles import finders


def design_page(request):
    if request.method == "POST":
        base_structure = request.POST.get("base_structure")
        color = request.POST.get("color")
        print_or_embroidery = request.POST.get("print_or_embroidery")
        phone_number = request.POST.get("phone_number")
        telegram = request.POST.get("telegram")
        comment = request.POST.get("comment")
        design_image = request.FILES.get("design_image")

        # Используем finders для получения путей к статическим файлам
        base_structure_path = finders.find(f"your_design/img/{base_structure}.PNG")
        color_path = finders.find(f"your_design/img/{color}.JPG")

        # Формируем HTML сообщение
        message = f"""
        <html>
        <body>
            <p>Базова структура: {base_structure}</p>
            <p>Колір: {color}</p>
            <p>Прінт або вишивка: {print_or_embroidery}</p>
            <p>Ваш телеграм: {telegram}</p>
            <p>Номер телефону: {phone_number}</p>
            <p>Коментар: {comment}</p>
        </body>
        </html>
        """

        email = EmailMessage(
            "Дизайн від користувача",
            message,
            settings.EMAIL_HOST_USER,
            ["danilgubarev9804@gmail.com"],
        )
        email.content_subtype = "html"  # Для отправки HTML письма

        # Прикрепление выбранных изображений
        if base_structure_path:
            with open(base_structure_path, "rb") as f:
                email.attach(f"{base_structure}.PNG", f.read(), "image/png")
        if color_path:
            with open(color_path, "rb") as f:
                email.attach(f"{color}.JPG", f.read(), "image/jpeg")

        # Прикрепление пользовательского изображения, если оно есть
        if design_image:
            email.attach(
                design_image.name, design_image.read(), design_image.content_type
            )

        email.send()

    return render(request, "your_design/design.html")
