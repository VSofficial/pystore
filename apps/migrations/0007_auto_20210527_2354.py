# Generated by Django 3.1.7 on 2021-05-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20210527_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appmodel',
            name='category',
            field=models.CharField(choices=[('ML', 'Machine Learning'), ('BIGDATA', 'Big Data'), ('AUTOMATION', 'Automation'), ('OPENCV', 'Image/Video Processing'), ('PRODUCTIVITY', 'Productivity / Office Tools'), ('DATASCIENCE', 'Data Science'), ('DRIVERS', 'Drivers/Database/System Programs'), ('DATAPROCESSING', 'Data Processing'), ('MISC', 'Others')], default='MISC', max_length=100),
        ),
    ]