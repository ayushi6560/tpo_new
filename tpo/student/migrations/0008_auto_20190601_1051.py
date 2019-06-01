# Generated by Django 2.2.1 on 2019-06-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190601_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sem',
            field=models.PositiveIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('5', '5'), ('4', '4'), ('8', '8'), ('7', '7'), ('', 'select'), ('6', '6')], default=5, null=True, verbose_name='Semesert'),
        ),
    ]