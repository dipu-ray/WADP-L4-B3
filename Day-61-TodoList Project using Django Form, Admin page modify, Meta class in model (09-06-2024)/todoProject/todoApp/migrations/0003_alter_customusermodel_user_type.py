# Generated by Django 5.0.6 on 2024-06-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_taskmodel_alter_customusermodel_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='user_type',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], max_length=100),
        ),
    ]
