# Generated by Django 5.0.4 on 2024-04-19 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_name_computer_computer_specification_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='user',
            new_name='name',
        ),
    ]
