# Generated by Django 3.0.8 on 2020-07-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sEndpoint', models.CharField(default='https://secure.logmeinrescue.com/api/', max_length=40)),
                ('sEmail', models.EmailField(default='gorkem.korkmaz@rigosis.com', max_length=254)),
                ('sPwd', models.CharField(default='FhG8AWyWdgry8uTUVj65.', max_length=25)),
                ('iSession', models.CharField(default=12345678, max_length=25)),
                ('iNodeID', models.CharField(default=337366, max_length=25)),
                ('sAuthCode', models.CharField(default='4ahx...80u0', max_length=25)),
            ],
        ),
    ]