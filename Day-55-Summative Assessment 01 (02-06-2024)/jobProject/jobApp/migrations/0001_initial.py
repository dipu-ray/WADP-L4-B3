# Generated by Django 5.0.6 on 2024-06-02 06:36

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('seeker', 'Job Seeker'), ('recruiter', 'Job Recruiter')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('others', 'Others')], max_length=100)),
                ('profile_picture', models.ImageField(upload_to='media/profile_picture')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('company_description', models.TextField()),
                ('company_logo', models.ImageField(upload_to='media/company_logo')),
                ('company_name', models.CharField(max_length=100)),
                ('company_location', models.TextField()),
                ('qualifications', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('salary', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_location', models.CharField(max_length=100)),
                ('company_details', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=100)),
                ('recruiter_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recruitermodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerEducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(max_length=100)),
                ('edu_institute', models.CharField(max_length=100)),
                ('edu_location', models.CharField(max_length=100)),
                ('seeker_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seekeredumodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('hobby', models.CharField(max_length=100)),
                ('seeker_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seekermodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeekerWorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(max_length=100)),
                ('work_location', models.CharField(max_length=100)),
                ('work_time', models.CharField(max_length=100)),
                ('seeker_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seekereorkmodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
