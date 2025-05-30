# Generated by Django 5.0.4 on 2024-04-25 06:25

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
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(upload_to='media/profile_pic')),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=100)),
                ('blood_group', models.CharField(choices=[('a+', 'A Positive'), ('a-', 'A Negative'), ('b+', 'B Positive'), ('b-', 'B Negative'), ('ab+', 'AB Positive'), ('ab-', 'AB Negative'), ('o+', 'O Positive'), ('o-', 'O Negative')], max_length=100)),
                ('user_type', models.CharField(choices=[('recruiter', 'Job Recruiter'), ('seeker', 'Job Seeker')], max_length=100)),
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
                ('Job_title', models.CharField(max_length=100)),
                ('Company_name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Company_description', models.TextField()),
                ('Job_description', models.TextField()),
                ('Qualification', models.CharField(max_length=100)),
                ('Salary_information', models.CharField(max_length=100)),
                ('Deadline', models.DateField(auto_now_add=True)),
                ('Designation', models.CharField(max_length=100)),
                ('Experience', models.CharField(max_length=100)),
                ('Recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
