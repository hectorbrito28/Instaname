# Generated by Django 4.2.7 on 2023-11-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userweb',
            name='website',
            field=models.URLField(blank=True, max_length=254),
        ),
    ]
