# Generated by Django 3.2 on 2021-05-14 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0005_mascota_publicar'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='comentario',
            field=models.TextField(default='--', null=True),
        ),
    ]
