# Generated by Django 2.1.1 on 2018-10-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0008_auto_20181002_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigla',
            name='descrizione',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='traduzione',
            name='traduzione',
            field=models.CharField(max_length=60),
        ),
    ]
