# Generated by Django 3.1.5 on 2021-08-28 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210827_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(max_length=140, null=True),
        ),
    ]
