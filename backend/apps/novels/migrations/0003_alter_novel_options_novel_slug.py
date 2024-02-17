# Generated by Django 5.0.2 on 2024-02-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0002_chapter_created_at_chapter_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='novel',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='novel',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]
