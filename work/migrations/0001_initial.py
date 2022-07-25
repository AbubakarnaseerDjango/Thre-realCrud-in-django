# Generated by Django 4.0.6 on 2022-07-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('lastName', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=500)),
                ('delivered', models.BooleanField(default=False)),
            ],
        ),
    ]
