# Generated by Django 5.1 on 2024-08-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='shop.productcategory'),
        ),
    ]
