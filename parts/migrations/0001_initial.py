# Generated by Django 3.1.6 on 2021-02-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('car_model', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('desciption', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='parts/images/')),
            ],
        ),
    ]
