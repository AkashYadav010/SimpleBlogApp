# Generated by Django 2.1.7 on 2019-03-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
