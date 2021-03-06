# Generated by Django 3.1.2 on 2020-10-21 23:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20201021_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='favorites',
        ),
        migrations.RemoveField(
            model_name='video',
            name='upvoted',
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='video_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
