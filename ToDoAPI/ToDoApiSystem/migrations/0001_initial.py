# Generated by Django 3.0.10 on 2021-05-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=300)),
                ('duedate', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
