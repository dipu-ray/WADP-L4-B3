# Generated by Django 5.0.6 on 2024-06-05 04:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0004_alter_applyjobmodel_qualifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjobmodel',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicantinfo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('others', 'Others'), ('male', 'Male')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='user_type',
            field=models.CharField(choices=[('seeker', 'Job Seeker'), ('recruiter', 'Job Recruiter')], max_length=100),
        ),
    ]
