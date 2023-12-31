# Generated by Django 4.2.4 on 2023-08-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.BooleanField(default=False, editable=False, verbose_name='current status')),
                ('last_checked', models.DateTimeField(auto_now=True, verbose_name='last time of checking status')),
                ('check_interval', models.PositiveIntegerField(default=10, verbose_name='check interval in minutes')),
                ('service_name', models.CharField(max_length=50, verbose_name='service name')),
                ('service_type', models.CharField(max_length=50, verbose_name='service type')),
                ('service_ip', models.GenericIPAddressField(verbose_name='service IP')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.BooleanField(default=False, editable=False, verbose_name='current status')),
                ('last_checked', models.DateTimeField(auto_now=True, verbose_name='last time of checking status')),
                ('check_interval', models.PositiveIntegerField(default=10, verbose_name='check interval in minutes')),
                ('website_name', models.CharField(max_length=50, verbose_name='website name')),
                ('website_url', models.URLField(verbose_name='website URL')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
