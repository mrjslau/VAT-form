# Generated by Django 2.0.5 on 2018-05-23 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=80)),
                ('units', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('price', models.FloatField()),
                ('totalPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchasesForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VATInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=5)),
                ('seller', models.CharField(max_length=100)),
                ('totalSum', models.IntegerField()),
                ('date', models.DateField()),
                ('purchases', models.ManyToManyField(to='vatforms.Purchase')),
            ],
        ),
    ]
