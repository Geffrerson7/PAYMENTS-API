# Generated by Django 4.1.4 on 2022-12-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appservices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AddField(
            model_name='service',
            name='prefixe',
            field=models.CharField(default='', max_length=200),
        ),
    ]
