# Generated by Django 3.0.3 on 2020-04-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_App', '0003_auto_20200423_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecords',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
