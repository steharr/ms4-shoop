# Generated by Django 3.2 on 2022-01-25 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
