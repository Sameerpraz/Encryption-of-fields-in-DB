# Generated by Django 3.1.6 on 2021-02-15 08:05

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20210215_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=100)),
        ),
    ]
