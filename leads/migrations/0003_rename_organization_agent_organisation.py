# Generated by Django 5.1.5 on 2025-02-23 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_userprofile_agent_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='organization',
            new_name='organisation',
        ),
    ]
