# Generated by Django 3.2 on 2021-05-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0010_galeria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='comentario',
            field=models.TextField(default='--'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='dueno',
            field=models.CharField(default='--', max_length=45),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='usuario',
            field=models.CharField(default='--', max_length=45),
        ),
    ]
