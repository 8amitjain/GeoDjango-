# Generated by Django 3.1.2 on 2020-10-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deed', '0017_salesdeed_representy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesdeedrepresentative',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='salesdeedrepresentative',
            name='representative_unique_id',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]