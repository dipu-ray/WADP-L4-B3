# Generated by Django 5.0.6 on 2024-06-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0008_alter_categorymodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='user_type',
            field=models.CharField(choices=[('user', 'User'), ('admin', 'Admin')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_priority',
            field=models.CharField(choices=[('hig', 'High'), ('low', 'Low'), ('medium', 'Medium')], max_length=100, null=True),
        ),
    ]
