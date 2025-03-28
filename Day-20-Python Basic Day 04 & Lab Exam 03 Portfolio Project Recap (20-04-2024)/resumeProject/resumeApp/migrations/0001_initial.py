# Generated by Django 5.0.3 on 2024-04-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeEducationModel',
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
                ('Profile_picture', models.ImageField(upload_to='media/ProfilePic')),
                ('Full_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('Email_address', models.CharField(max_length=100)),
                ('Career_objective', models.TextField()),
                ('Hard_Skills', models.CharField(max_length=100)),
                ('Soft_Skills', models.CharField(max_length=100)),
                ('Certifications', models.CharField(max_length=100)),
                ('Projects', models.CharField(max_length=100)),
                ('References', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeWorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Start_dates', models.CharField(max_length=100)),
                ('End_dates', models.CharField(max_length=100)),
            ],
        ),
    ]
