# Generated by Django 2.1.7 on 2019-02-23 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_auto_20190223_2338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'type', 'verbose_name_plural': 'types'},
        ),
    ]
