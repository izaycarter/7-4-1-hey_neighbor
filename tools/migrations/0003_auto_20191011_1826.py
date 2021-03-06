# Generated by Django 2.2.6 on 2019-10-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_auto_20191010_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='type',
            field=models.CharField(choices=[('HAND TOOL', 'Hand Tool'), ('GARDEN TOOL', 'Garden Tool'), ('POWER TOOL', 'Power Tool')], default='HAND TOOL', max_length=255),
        ),
        migrations.AlterField(
            model_name='tool',
            name='is_available',
            field=models.BooleanField(default='False'),
        ),
    ]
