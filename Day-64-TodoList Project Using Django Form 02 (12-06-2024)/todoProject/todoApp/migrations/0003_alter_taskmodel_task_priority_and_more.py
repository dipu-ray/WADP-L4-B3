# Generated by Django 5.0.6 on 2024-06-12 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_alter_taskmodel_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task_priority',
            field=models.CharField(choices=[('low', 'Low'), ('hig', 'High'), ('medium', 'Medium')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_status',
            field=models.CharField(default='On Going', max_length=100, null=True),
        ),
    ]
