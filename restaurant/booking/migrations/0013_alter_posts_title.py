# Generated by Django 4.0.4 on 2022-05-22 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_subsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
