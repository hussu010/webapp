# Generated by Django 2.2.3 on 2019-09-22 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0016_auto_20190922_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]