# Generated by Django 3.1.7 on 2022-01-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_auto_20220105_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='image',
            field=models.ImageField(upload_to='screenshots'),
            preserve_default=False,
        ),
    ]
