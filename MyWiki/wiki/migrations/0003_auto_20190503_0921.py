# Generated by Django 2.2 on 2019-05-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20190501_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='id',
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]
