# Generated by Django 3.0.3 on 2020-08-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_App', '0007_auto_20200809_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='appeared_by',
            field=models.TextField(blank=True),
        ),
    ]
