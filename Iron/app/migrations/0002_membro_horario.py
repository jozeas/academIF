# Generated by Django 4.2.6 on 2023-12-04 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membro',
            name='horario',
            field=models.TimeField(default='20:58:17'),
        ),
    ]