# Generated by Django 5.0.7 on 2024-08-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=200)),
                ('about_description', models.TextField()),
                ('about_image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='Accueil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('accueil_text1', models.TextField()),
                ('accueil_text2', models.TextField()),
                ('accueil_bouton', models.TextField()),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_title', models.CharField(max_length=200)),
                ('evaluation_description', models.TextField()),
                ('text_calcul', models.TextField()),
                ('description_calcul', models.TextField()),
                ('text_demo', models.TextField()),
                ('image1', models.ImageField(upload_to='evalutation/')),
                ('image2', models.ImageField(upload_to='evalutation/')),
                ('image3', models.ImageField(upload_to='evalutation/')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onglet1', models.CharField(max_length=100)),
                ('onglet2', models.CharField(max_length=100)),
                ('onglet3', models.CharField(max_length=100)),
                ('onglet4', models.CharField(max_length=100)),
            ],
        ),
    ]
