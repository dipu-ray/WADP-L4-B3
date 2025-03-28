# Generated by Django 5.0.6 on 2024-06-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_alter_taskmodel_task_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('hig', 'High')], max_length=100, null=True),
        ),
    ]
