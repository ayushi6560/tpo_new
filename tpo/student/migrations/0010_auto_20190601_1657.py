# Generated by Django 2.2.1 on 2019-06-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20190601_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sem',
            field=models.PositiveIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('6', '6'), ('', 'select'), ('8', '8'), ('5', '5'), ('7', '7'), ('4', '4')], null=True, verbose_name='Semesert'),
        ),
    ]
