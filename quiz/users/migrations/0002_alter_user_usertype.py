# Generated by Django 4.2.3 on 2023-07-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertype',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], default='USER', max_length=10),
        ),
    ]
