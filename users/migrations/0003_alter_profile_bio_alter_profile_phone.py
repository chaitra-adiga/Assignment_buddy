# Generated by Django 5.1.1 on 2024-11-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_phone_profile_upi_id_alter_profile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]