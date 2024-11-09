# Generated by Django 5.0.6 on 2024-11-09 16:21

import django.core.validators
import django.db.models.deletion
import main.mixins
import products.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            bases=(main.mixins.SaveSlugMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('available_colors', models.JSONField(default=list)),
                ('available_sizes', models.JSONField(default=list, validators=[products.validators.ProductSizeValidator.validate_size])),
                ('available', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('shoes', 'shoes'), ('t-shirt', 't-shirt'), ('sweatshirt', 'sweatshirt'), ('pants', 'pants'), ('jacket', 'jacket'), ('sunglasses', 'sunglasses')], max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.collection')),
            ],
            bases=(main.mixins.SaveSlugMixin, models.Model),
        ),
    ]
