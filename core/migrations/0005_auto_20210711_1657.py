# Generated by Django 3.0.7 on 2021-07-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_follow_is_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='followed',
        ),
    ]