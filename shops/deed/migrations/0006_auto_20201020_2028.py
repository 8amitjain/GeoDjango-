# Generated by Django 3.1.2 on 2020-10-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0005_auto_20201020_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earning',
            name='earning',
            field=models.CharField(max_length=3),
        ),
    ]