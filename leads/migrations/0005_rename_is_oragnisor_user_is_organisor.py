# Generated by Django 5.1.6 on 2025-02-27 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_user_is_agent_user_is_oragnisor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_oragnisor',
            new_name='is_organisor',
        ),
    ]
