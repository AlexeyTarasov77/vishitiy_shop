import random

# Импортируем модуль random для генерации случайных данных
from django.core.management.base import BaseCommand

# Импортируем BaseCommand для создания пользовательских команд Django
# Импортируем настройки из конфигурации Django
from faker import Faker

# Импортируем Faker для генерации фейковых данных
from products.models import Collection, Product

# Импортируем модели Django


class Command(BaseCommand):
    """Management команда для наполнения базы данных.
    Используется библиотека faker для генерации случайных данных.
    Запуск: python manage.py create_products.
    """

    def handle(self, *args, **kwargs):
        fake = Faker()
        # Создаем экземпляр Faker для генерации фейковых данных

        # Цикл для создания 10 фейковых объектов Collection
        for _ in range(15):
            Collection.objects.create(
                name=fake.name(),  # Генерируем фейковое название для коллекции
                image=random.choice(
                    [
                        "IMG_6319.JPG_xfH9C6R_zYeW65m.jpg",
                        "IMG_6459.JPG.jpg",
                        "IMG_8511_apDQ2iL.PNG",
                        "IMG_8973.PNG",
                    ]
                ),  # Генерируем фейковый URL изображения для коллекции
                description=fake.text(),  # Генерируем фейковое описание для коллекции
            )

            # Создаем объект Product
            Product.objects.create(
                title=fake.name(),
                available_colors=random.sample(
                    [color[0] for color in Product.COLOR_PALETTE], 3
                ),
                available_sizes=random.sample(Product.ACCEPTABLE_SIZES, 3),
                type=random.choice(Product.PRODUCT_TYPE_CHOICES)[0],
                discount=random.choice([0, 10, 20, 50]),
                image=random.choice(
                    [
                        "IMG_6319.JPG_xfH9C6R_zYeW65m.jpg",
                        "IMG_6459.JPG.jpg",
                        "IMG_8511_apDQ2iL.PNG",
                        "IMG_8973.PNG",
                    ]
                ),
                description=fake.text(),
                price=fake.random_int(min=100, max=5000),
                collection=random.choice(Collection.objects.all()),
            )
