# Generated by Django 2.1.2 on 2021-03-26 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customreport',
            name='customuser',
        ),
        migrations.DeleteModel(
            name='CustomReport',
        ),
    ]
