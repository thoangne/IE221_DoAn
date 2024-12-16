# Generated by Django 5.1.3 on 2024-12-14 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=10)),
                ('hire_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('contact_info', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('dosage_form', models.CharField(max_length=10)),
                ('strength', models.CharField(max_length=10)),
                ('quantity_in_stock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.category')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('quantity_sold', models.IntegerField()),
                ('sale_date', models.DateField()),
                ('total', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.customer')),
                ('medicine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicines.medicine')),
            ],
        ),
    ]
