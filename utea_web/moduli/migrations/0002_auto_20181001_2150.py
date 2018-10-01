# Generated by Django 2.1.1 on 2018-10-01 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_lingua'),
        ('moduli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sigla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5)),
                ('descrizione', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'sigle',
            },
        ),
        migrations.CreateModel(
            name='Sigla_Traduzioni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traduzione', models.CharField(max_length=30)),
                ('lingua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lingua')),
                ('sigla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traduzioni', to='moduli.Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('prefisso', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'verbose_name': 'tipologia di componente',
                'verbose_name_plural': 'tipologie di componenti',
            },
        ),
        migrations.AddField(
            model_name='sigla',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduli.Tipo_componente'),
        ),
    ]
