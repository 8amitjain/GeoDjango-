# Generated by Django 3.1.2 on 2020-10-20 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0004_auto_20201020_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='position',
        ),
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.FloatField(blank=True, null=True),
        ),
    ]