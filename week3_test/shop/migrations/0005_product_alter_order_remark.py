# Generated by Django 5.1 on 2024-08-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(null=True)),
                ('remaining_amount', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='remark',
            field=models.TextField(null=True),
        ),
    ]
