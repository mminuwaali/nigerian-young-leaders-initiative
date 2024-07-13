# Generated by Django 5.0.3 on 2024-04-11 21:07

import markdownx.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('description', markdownx.models.MarkdownxField(default='')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=2000)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
