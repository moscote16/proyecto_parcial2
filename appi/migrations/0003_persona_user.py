# Generated by Django 4.2.1 on 2023-05-19 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appi', '0002_persona_producto_ventas_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
