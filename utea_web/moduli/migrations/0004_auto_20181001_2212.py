# Generated by Django 2.1.1 on 2018-10-01 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduli', '0003_auto_20181001_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='traduzione',
            options={'verbose_name_plural': 'traduzioni'},
        ),
        migrations.RemoveField(
            model_name='traduzione',
            name='sigla',
        ),
        migrations.AddField(
            model_name='sigla',
            name='traduzione',
            field=models.ManyToManyField(to='moduli.Traduzione'),
        ),
    ]
