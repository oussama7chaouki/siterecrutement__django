# Generated by Django 4.2.7 on 2023-12-02 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recruter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
                ('prenom', models.CharField(blank=True, max_length=250, null=True)),
                ('ville', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=191, null=True)),
                ('_select', models.CharField(blank=True, max_length=100, null=True)),
                ('cv', models.FileField(null=True, upload_to='cv/')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]