# Generated by Django 3.1.7 on 2022-01-08 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_remove_userregistrationmodel_date_of_birth'),
        ('apps', '0017_auto_20220105_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.userregistrationmodel')),
            ],
        ),
    ]