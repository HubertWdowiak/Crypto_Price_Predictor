# Generated by Django 3.0.5 on 2020-05-09 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_auto_20200509_0901'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coin',
        ),
        migrations.DeleteModel(
            name='CoinForTable',
        ),
    ]
