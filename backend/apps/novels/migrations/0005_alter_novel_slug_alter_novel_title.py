# Generated by Django 5.0.3 on 2024-08-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0004_alter_novel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255, unique=True), max_length=255),
        ),
        migrations.AlterField(
            model_name='novel',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
