# Generated by Django 5.1 on 2024-08-25 10:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0003_alter_mensaje_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='fecha_hora',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]