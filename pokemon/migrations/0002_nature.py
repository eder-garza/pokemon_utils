# Generated by Django 2.1.7 on 2019-03-02 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial_squash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, unique=True)),
                ('positive', models.CharField(max_length=16, null=True)),
                ('negative', models.CharField(max_length=16, null=True)),
            ],
        ),
    ]
