# Generated by Django 2.2.3 on 2019-09-20 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_todo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]