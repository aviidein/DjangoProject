# Generated by Django 2.2.7 on 2019-12-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='police',
            fields=[
                ('thana', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
