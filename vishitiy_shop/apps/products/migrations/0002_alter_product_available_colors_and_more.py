# Generated by Django 5.0.6 on 2024-11-13 07:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_colors'
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_sizes'
        ),
        migrations.AddField(
            model_name='product',
            name='available_colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(choices=[('white', 'white'), ('black', 'black'), ('red', 'red'), ('green', 'green'), ('blue', 'blue'), ('yellow', 'yellow')]), default=list, size=6),
        ),
        migrations.AddField(
            model_name='product',
            name='available_sizes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')]), default=list, size=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]