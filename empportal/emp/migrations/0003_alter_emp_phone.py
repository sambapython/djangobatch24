# Generated by Django 3.2.9 on 2021-11-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_alter_emp_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
