# Generated by Django 2.1.1 on 2018-09-11 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sigla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=5)),
                ('descrizione', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'sigle',
            },
        ),
        migrations.CreateModel(
            name='TipoComponente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('abbreviato', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'tipologia di componente',
                'verbose_name_plural': 'tipologie di componenti',
            },
        ),
        migrations.AddField(
            model_name='sigla',
            name='tipo_componente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduli.TipoComponente'),
        ),
    ]
