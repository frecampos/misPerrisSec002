# Generated by Django 3.2 on 2021-05-26 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misPerris', '0008_mascota_dueno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(default='fotos/no_disponible.jpg', upload_to='fotos'),
        ),
    ]
