# Generated by Django 3.0.2 on 2020-05-09 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20200509_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('username',)},
        ),
    ]
