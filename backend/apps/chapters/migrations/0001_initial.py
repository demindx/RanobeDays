# Generated by Django 5.0.3 on 2024-07-18 11:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('novels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('volume', models.IntegerField(default=1)),
                ('number', models.IntegerField(default=1)),
                ('text', models.TextField()),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novels.novel')),
            ],
            options={
                'db_table': 'chapters',
                'ordering': ['novel', '-created_at', 'team'],
                'default_related_name': 'chapters',
            },
        ),
    ]
