# Generated by Django 4.0.4 on 2022-06-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220606_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='Notificarme',
            new_name='is_Notificarme',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]