# Generated by Django 3.2 on 2024-11-24 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_auto_20241124_1038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journal',
            old_name='ececutor',
            new_name='executor',
        ),
    ]
