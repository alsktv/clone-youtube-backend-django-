# Generated by Django 5.0.4 on 2024-04-18 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('videos', '0002_video_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.video'),
        ),
    ]
