# Generated by Django 5.0.4 on 2024-05-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_video_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
