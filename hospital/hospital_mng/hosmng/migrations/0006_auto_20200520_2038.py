# Generated by Django 3.0 on 2020-05-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosmng', '0005_auto_20200520_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
