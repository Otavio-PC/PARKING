# Generated by Django 4.2.1 on 2023-05-26 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariomodel',
            name='garagens_em_uso',
        ),
    ]