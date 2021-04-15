# Generated by Django 3.2 on 2021-04-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('mobile_phone', models.CharField(blank=True, max_length=255, verbose_name='Mobile phone')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('baptize_date', models.DateField(blank=True, null=True, verbose_name='Baptize date')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('note', models.TextField(blank=True, verbose_name='Note')),
            ],
        ),
    ]
