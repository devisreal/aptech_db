# Generated by Django 4.0.6 on 2022-09-03 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_is_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='is_completed',
        ),
    ]
