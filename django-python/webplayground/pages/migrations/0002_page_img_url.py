# Generated by Django 2.1.7 on 2019-05-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='img_url',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Imagen'),
        ),
    ]
