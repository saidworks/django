# Generated by Django 3.2.7 on 2021-09-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20210914_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN_10', models.CharField(max_length=10)),
                ('ISBN_13', models.CharField(max_length=13)),
            ],
        ),
    ]