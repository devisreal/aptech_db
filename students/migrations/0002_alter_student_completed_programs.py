# Generated by Django 4.0.6 on 2022-08-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='completed_programs',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
