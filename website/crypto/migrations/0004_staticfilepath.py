# Generated by Django 3.0.5 on 2020-05-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0003_auto_20200502_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticFilePath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_id', models.CharField(default='default_id', max_length=10)),
                ('path', models.CharField(default='/', max_length=10)),
            ],
        ),
    ]
