# Generated by Django 3.2.9 on 2021-11-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0004_alter_emp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]