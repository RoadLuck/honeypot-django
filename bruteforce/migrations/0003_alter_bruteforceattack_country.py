# Generated by Django 4.1.7 on 2023-03-17 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruteforce', '0002_bruteforceattack_country_bruteforceattack_is_success'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bruteforceattack',
            name='country',
            field=models.CharField(blank=True, default='N-N', max_length=3, null=True),
        ),
    ]
