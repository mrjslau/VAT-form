# Generated by Django 2.0.5 on 2018-05-23 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vatforms', '0002_vatinvoice_owner'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PurchasesForm',
            new_name='PurchasesWriteOffForm',
        ),
    ]
