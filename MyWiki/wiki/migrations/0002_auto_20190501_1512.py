# Generated by Django 2.2 on 2019-05-01 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='wiki',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='Title',
            new_name='title',
        ),
    ]
