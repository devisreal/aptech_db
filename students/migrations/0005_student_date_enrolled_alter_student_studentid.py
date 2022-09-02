# Generated by Django 4.0.6 on 2022-08-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_studentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_enrolled',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentId',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]