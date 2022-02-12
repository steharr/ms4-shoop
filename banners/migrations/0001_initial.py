# Generated by Django 3.2 on 2022-02-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=254)),
                ('theme', models.CharField(max_length=1)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('price_threshold', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
