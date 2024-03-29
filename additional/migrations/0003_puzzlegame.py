# Generated by Django 4.1.3 on 2022-12-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('additional', '0002_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuzzleGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timer', models.IntegerField(blank=True, max_length=5, null=True)),
                ('win_state', models.TextField(blank=True, max_length=256, null=True)),
                ('lose_state', models.TextField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
