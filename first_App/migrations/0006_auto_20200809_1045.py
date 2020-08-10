# Generated by Django 3.0.3 on 2020-08-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_App', '0005_auto_20200702_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='category', max_length=264)),
                ('question', models.CharField(default='question', max_length=264)),
                ('option1', models.CharField(default='opt1', max_length=264)),
                ('option2', models.CharField(default='opt2', max_length=264)),
                ('option3', models.CharField(default='opt3', max_length=264)),
                ('option4', models.CharField(default='opt4', max_length=264)),
                ('option_correct', models.CharField(default='opt_correct', max_length=264)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
    ]
