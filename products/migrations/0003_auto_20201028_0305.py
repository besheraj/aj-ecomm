# Generated by Django 3.1.2 on 2020-10-28 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201022_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=1024, null=True),
        ),
    ]
