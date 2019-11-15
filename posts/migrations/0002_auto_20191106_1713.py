# Generated by Django 2.2.3 on 2019-11-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='title',
            new_name='subject',
        ),
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Subject'),
        ),
    ]
