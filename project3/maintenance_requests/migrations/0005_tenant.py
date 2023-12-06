# Generated by Django 4.2.6 on 2023-12-06 16:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance_requests', '0004_alter_maintenance_request_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_check_in', models.DateTimeField()),
                ('date_check_out', models.DateTimeField()),
                ('apartment_number', models.IntegerField(max_length=5)),
            ],
        ),
    ]
