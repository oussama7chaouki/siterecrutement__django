# Generated by Django 4.2.7 on 2023-12-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='cv',
            field=models.FileField(null=True, upload_to='cv/'),
        ),
    ]
