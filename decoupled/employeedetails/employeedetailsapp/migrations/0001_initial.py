# Generated by Django 4.0.5 on 2023-05-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('place', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
