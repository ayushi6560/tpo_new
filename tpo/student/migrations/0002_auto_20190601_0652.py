# Generated by Django 2.2.1 on 2019-06-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sem',
            field=models.PositiveIntegerField(choices=[('4', '4'), ('7', '7'), ('2', '2'), ('8', '8'), ('5', '5'), ('6', '6'), ('1', '1'), ('3', '3'), ('', 'select')], default=5, verbose_name='Semesert'),
        ),
    ]
