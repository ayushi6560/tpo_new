# Generated by Django 2.2.1 on 2019-06-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20190601_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sem',
            field=models.PositiveIntegerField(choices=[(2, '2'), (5, '5'), (7, '7'), ('', 'select'), (6, '6'), (3, '3'), (4, '4'), (8, '8'), (1, '1')], null=True, verbose_name='Semesert'),
        ),
    ]