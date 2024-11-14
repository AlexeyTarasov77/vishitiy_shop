import os
import random

from django.core.management.base import BaseCommand, CommandError, CommandParser
from faker import Faker
from products.models import Collection, Product


class Command(BaseCommand):
    help = "Creates specified number of collections and products"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "count", type=int, help="Number of collections and products to create", default=10
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        if count < 1:
            raise CommandError("Count must be at least 1")
        if count > 1000:
            self.stdout.write(self.style.WARNING("Warning: it can take a while"))
        fake = Faker()

        def get_images(dirname: str) -> list[str]:
            path = os.path.join(os.path.dirname(__file__), "images", dirname)
            return os.listdir(path)

        collection_images = get_images("collections")
        product_images = get_images("products")
        self.stdout.write(self.style.NOTICE(f"Creating {count} collections and products"))
        for _ in range(count):
            # TODO: Remove hardcoded img names
            Collection.objects.create(
                name=fake.name(),
                image=random.choice(collection_images),
                description=fake.text(),
            )

            Product.objects.create(
                title=fake.name(),
                available_colors=random.sample(Product.VALID_COLORS, 3),
                available_sizes=random.sample(Product.VALID_SIZES, 3),
                category=random.choice(Product.VALID_CATEGORIES),
                discount=random.choice([0, 10, 20, 50]),
                image=random.choice(product_images),
                description=fake.text(),
                price=fake.random_int(min=100, max=5000),
                collection_id=random.choice(Collection.objects.values_list("id", flat=True)),
            )
        self.stdout.write(self.style.SUCCESS(f"Created {count} collections and products"))
