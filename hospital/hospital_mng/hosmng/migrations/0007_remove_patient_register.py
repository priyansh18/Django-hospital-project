# Generated by Django 3.0 on 2020-05-20 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosmng', '0006_auto_20200520_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='register',
        ),
    ]
