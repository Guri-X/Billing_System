# Generated by Django 3.1.6 on 2021-03-13 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('product_cost', models.CharField(max_length=100)),
                ('product_company', models.CharField(max_length=100)),
                ('product_stock', models.CharField(max_length=100)),
            ],
        ),
    ]
