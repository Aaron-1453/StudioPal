# Generated by Django 3.1.2 on 2020-10-22 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_video_paypal_donate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='paypal_donate',
            new_name='paypal_url_to_receive_donation',
        ),
    ]
