# Generated by Django 5.0.6 on 2024-06-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('others', 'Others')], max_length=100),
        ),
    ]
