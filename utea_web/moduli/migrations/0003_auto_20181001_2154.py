# Generated by Django 2.1.1 on 2018-10-01 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_lingua'),
        ('moduli', '0002_auto_20181001_2150'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sigla_Traduzioni',
            new_name='Traduzione',
        ),
    ]
