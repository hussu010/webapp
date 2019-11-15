# Generated by Django 2.2.3 on 2019-11-08 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191106_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.Level'),
        ),
    ]
