# Generated by Django 4.1.7 on 2023-03-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('code', models.TextField()),
                ('phone', models.IntegerField()),
                ('description', models.TextField())
            ],
        ),
    ]
