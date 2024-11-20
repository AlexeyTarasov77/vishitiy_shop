from decimal import Decimal

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from main.mixins import SaveSlugMixin


class Product(SaveSlugMixin, models.Model):
    slugify_field_name = "title"

    VALID_SIZES = ("XS", "S", "M", "L", "XL", "XXL")
    SIZE_CHOICES = tuple((_(size), size) for size in VALID_SIZES)
    VALID_COLORS = ("white", "black", "red", "green", "blue", "yellow")
    COLOR_CHOICES = tuple((color, _(color).capitalize()) for color in VALID_COLORS)
    VALID_CATEGORIES = ("shoes", "t-shirt", "sweatshirt", "pants", "jacket", "sunglasses")
    CATEGORY_CHOICES = tuple((cat, _(cat).capitalize()) for cat in VALID_CATEGORIES)

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    available_colors = ArrayField(
        models.TextField(choices=COLOR_CHOICES), default=list, size=len(COLOR_CHOICES)
    )
    available_sizes = ArrayField(
        models.TextField(choices=SIZE_CHOICES), default=list, size=len(SIZE_CHOICES)
    )
    available = models.BooleanField(default=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    image = models.ImageField()
    description = models.TextField(blank=True, default="")
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

    def get_absolute_url(self) -> str:
        return reverse("products:detail", kwargs={"slug": self.slug})

    @property
    def image_url(self) -> str:
        return self.image.url

    @property
    def final_price(self) -> Decimal:
        return self.price - (self.price * self.discount / 100)

    @property
    def url(self) -> str:
        return self.get_absolute_url()


class Collection(SaveSlugMixin, models.Model):
    slugify_field_name = "name"

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()
    description = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.name
