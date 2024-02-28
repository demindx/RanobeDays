# Generated by Django 5.0.2 on 2024-02-27 21:15

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novels', '0005_delete_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novels.novel')),
            ],
            options={
                'db_table': 'chapters',
                'ordering': ['novel', '-created_at'],
                'default_related_name': 'chapters',
            },
        ),
    ]