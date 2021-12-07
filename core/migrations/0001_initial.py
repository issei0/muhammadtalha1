# Generated by Django 3.2.9 on 2021-12-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email_address', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('button', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('copyright', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('text1', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('desc', models.TextField(blank=True, null=True)),
                ('button1', models.CharField(blank=True, max_length=200, null=True)),
                ('link1', models.URLField(blank=True, null=True)),
                ('button2', models.CharField(blank=True, max_length=200, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('text1', models.CharField(blank=True, max_length=200, null=True)),
                ('text2', models.CharField(blank=True, max_length=200, null=True)),
                ('text3', models.CharField(blank=True, max_length=200, null=True)),
                ('text4', models.CharField(blank=True, max_length=200, null=True)),
                ('homeimage', models.ImageField(blank=True, null=True, upload_to='')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, null=True)),
                ('button1', models.CharField(blank=True, max_length=200, null=True)),
                ('link1', models.URLField(blank=True, null=True)),
                ('button2', models.CharField(blank=True, max_length=200, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
