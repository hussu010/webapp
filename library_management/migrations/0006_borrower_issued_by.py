# Generated by Django 2.2.3 on 2020-03-15 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library_management', '0005_auto_20200312_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='issued_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
