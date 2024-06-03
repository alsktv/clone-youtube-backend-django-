# Generated by Django 5.0.4 on 2024-05-21 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_alter_comment_review'),
        ('shorts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='content_video',
        ),
        migrations.AddField(
            model_name='comment',
            name='content_short',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shorts.shorts'),
        ),
    ]