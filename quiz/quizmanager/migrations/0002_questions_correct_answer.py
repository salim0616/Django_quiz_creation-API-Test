# Generated by Django 4.2.3 on 2023-07-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct_answer',
            field=models.CharField(default='', max_length=200),
        ),
    ]
