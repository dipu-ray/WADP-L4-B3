# Generated by Django 5.0.6 on 2024-06-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='gender',
            field=models.CharField(choices=[('others', 'Others'), ('female', 'Female'), ('male', 'Male')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='user_type',
            field=models.CharField(choices=[('seeker', 'Job Seeker'), ('recruiter', 'Job Recruiter')], max_length=100),
        ),
    ]
