# Generated by Django 4.2.1 on 2023-05-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appi', '0003_persona_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ventas',
            name='numero_ventas',
            field=models.BigIntegerField(),
        ),
    ]