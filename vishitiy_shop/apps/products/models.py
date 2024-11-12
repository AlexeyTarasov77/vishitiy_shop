from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from main.mixins import SaveSlugMixin

from products.validators import ProductSizeValidator


class Product(SaveSlugMixin, models.Model):
    slugify_field_name = "title"

    ACCEPTABLE_SIZES = ["XS", "S", "M", "L", "XL", "XXL"]
    SIZE_CHOICES = tuple((size, size) for size in ACCEPTABLE_SIZES)
    COLOR_PALETTE = tuple(
        (color, color) for color in ("white", "black", "red", "green", "blue", "yellow")
    )
    PRODUCT_TYPE_CHOICES = tuple(
        (type, type)
        for type in (
            "shoes",
            "t-shirt",
            "sweatshirt",
            "pants",
            "jacket",
            "sunglasses",
        )  # Варианты типов продуктов
    )

    SIZE_VALIDATOR = ProductSizeValidator(ACCEPTABLE_SIZES)

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    available_colors = models.JSONField(default=list)
    available_sizes = models.JSONField(default=list, validators=[SIZE_VALIDATOR.validate_size])
    available = models.BooleanField(default=True)
    type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=50)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)
    # TODO: использовать поле составного типа, для хранения валюты
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Discount in % from 0 to 100
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    collection = models.ForeignKey(
        "Collection",
        on_delete=models.CASCADE,
        related_name="products",
    )

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    @property
    def image_url(self):
        return self.image.url

    @property
    def final_price(self):
        return self.price - (self.price * self.discount / 100)

    @property
    def url(self):
        return self.get_absolute_url()


class Collection(SaveSlugMixin, models.Model):
    slugify_field_name = "name"

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
