import random

from django.db import transaction
from django.db.models import Model
from django.db.utils import IntegrityError
from pytils.translit import slugify


class SaveSlugMixin:
    """
    Mixin for automatic saving slug when saving a model object.
    Redefines the save method for saving an object model with generation and saving a unique slug.
    """

    slugify_field_name = None
    model_slug_field_name: str = "slug"

    def save(self, *args, **kwargs) -> None:
        if not isinstance(self, Model):
            raise TypeError("This mixin must be used with a model")
        if not self.slugify_field_name or not self.model_slug_field_name:
            raise ValueError(
                "slugify_field_name must be overwritten and model_slug_field_name can't be None."
            )
        slug = getattr(self, self.model_slug_field_name)
        if not slug:
            slugify_value = getattr(self, self.slugify_field_name)
            slug = slugify(slugify_value)

        def try_to_save_unique_slug(new_slug: str):
            setattr(self, self.model_slug_field_name, new_slug)
            try:
                # starting a new transaction every time, because in case of error during Model.save
                # calling save method again will cause an error. The reason is that
                # it will try to execute it in failed transaction, which can be just aborted
                with transaction.atomic():
                    # calling django.db.models.Model's save method to save model instance
                    return Model.save(self, *args, **kwargs)
            except IntegrityError as e:
                print("Slug already exists", e)
                # WARNING: random.randint
                return try_to_save_unique_slug(slug + str(random.randint(0, 1000)))

        return try_to_save_unique_slug(slug)
