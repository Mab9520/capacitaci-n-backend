# Generated by Django 3.1 on 2022-03-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_remove_workertypework_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
