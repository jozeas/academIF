# Generated by Django 4.2.6 on 2023-12-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_membro_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membro',
            name='horario',
            field=models.TimeField(null=True),
        ),
    ]
