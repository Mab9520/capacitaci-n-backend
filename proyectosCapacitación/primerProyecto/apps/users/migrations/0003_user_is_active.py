# Generated by Django 3.1 on 2022-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220228_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
