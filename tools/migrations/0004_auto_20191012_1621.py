# Generated by Django 2.2.6 on 2019-10-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20191011_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
