# Generated by Django 5.0.7 on 2024-08-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accueil',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
            preserve_default=False,
        ),
    ]
