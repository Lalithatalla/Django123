# Generated by Django 4.1 on 2023-05-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('saddr', models.CharField(max_length=60)),
            ],
        ),
    ]
