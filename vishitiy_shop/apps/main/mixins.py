import random

from django.db.models import Model
from pytils.translit import slugify


class SaveSlugMixin:
    """
    Mixin for automatic saving slug when saving a model object.
    Redefines the save method for saving an object model with generation and saving a unique slug.
    """

    def save(self, model_slug_field="slug", slugify_value=None, *args, **kwargs):
        if model_slug_field and slugify_value:
            slug = getattr(self, model_slug_field)
            if not slug:
                new_slug = slugify(slugify_value)
                setattr(self, model_slug_field, new_slug)
                model: Model = self.__class__
                # TODO: переработать так, что бы вместо проверки на существование сразу пытаться сохранять. И отлавлить ошибку в случае нарушения уникальности
                while model.objects.filter(**{model_slug_field + "__iexact": new_slug}).exists():
                    new_slug += str(random.randint(0, (self.__class__.objects.count() + 1) * 100))
                    setattr(self, model_slug_field, new_slug)
        return super().save(*args, **kwargs)
