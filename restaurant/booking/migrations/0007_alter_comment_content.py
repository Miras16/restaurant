# Generated by Django 4.0.4 on 2022-05-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
