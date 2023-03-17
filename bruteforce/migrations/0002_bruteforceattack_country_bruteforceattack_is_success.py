# Generated by Django 4.1.7 on 2023-03-17 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruteforce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bruteforceattack',
            name='country',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='bruteforceattack',
            name='is_success',
            field=models.BooleanField(default=False),
        ),
    ]
