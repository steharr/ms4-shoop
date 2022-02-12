# Generated by Django 3.2 on 2022-02-12 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='theme',
            field=models.CharField(choices=[('U', 'Urgent'), ('M', 'Moderate'), ('L', 'Reminder')], max_length=1),
        ),
    ]
