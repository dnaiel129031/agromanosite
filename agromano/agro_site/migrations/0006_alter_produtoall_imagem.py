# Generated by Django 5.1.1 on 2024-09-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro_site', '0005_produtoall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoall',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
