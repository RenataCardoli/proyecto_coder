# Generated by Django 3.1.7 on 2022-06-06 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220606_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='avisos',
            new_name='Notificarme',
        ),
    ]