# Generated by Django 2.2.7 on 2019-12-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeverification',
            name='C_tourist',
            field=models.CharField(default='', max_length=55),
        ),
        migrations.AlterField(
            model_name='policeverification',
            name='Tourist_M',
            field=models.CharField(default='', max_length=55),
        ),
    ]
