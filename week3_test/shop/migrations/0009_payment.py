# Generated by Django 5.1 on 2024-08-25 07:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shop.order')),
                ('payment_date', models.DateField()),
                ('remark', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
