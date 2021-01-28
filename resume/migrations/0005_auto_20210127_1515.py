# Generated by Django 3.1.5 on 2021-01-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_resume_experience_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='about',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='job',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='university',
            field=models.CharField(max_length=200, null=True),
        ),
    ]