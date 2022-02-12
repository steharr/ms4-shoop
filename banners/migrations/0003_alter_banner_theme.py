# Generated by Django 3.2 on 2022-02-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0002_alter_banner_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='theme',
            field=models.CharField(choices=[('U', 'Urgent'), ('M', 'Moderate'), ('L', 'Reminder')], default='U', max_length=1),
        ),
    ]
