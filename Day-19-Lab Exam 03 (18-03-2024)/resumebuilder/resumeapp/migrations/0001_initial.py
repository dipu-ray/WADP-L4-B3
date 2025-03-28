# Generated by Django 5.0.4 on 2024-04-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Degree', models.CharField(max_length=100)),
                ('Institution', models.CharField(max_length=100)),
                ('Graduation_year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_pic', models.ImageField(upload_to='media/resumeImg')),
                ('Full_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('Email_address', models.CharField(max_length=100)),
                ('Career_objective', models.CharField(max_length=100)),
                ('Hard_skills', models.CharField(max_length=100)),
                ('Soft_skills', models.CharField(max_length=100)),
                ('Certifications', models.CharField(max_length=100)),
                ('Projects', models.CharField(max_length=100)),
                ('References', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Start_date', models.CharField(max_length=100)),
                ('End_date', models.CharField(max_length=100)),
            ],
        ),
    ]
