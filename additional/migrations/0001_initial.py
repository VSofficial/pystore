# Generated by Django 4.1.3 on 2022-11-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=254, null=True)),
                ('subTitle', models.TextField(blank=True, max_length=128, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('time_frame', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]