# Generated by Django 4.0 on 2022-11-17 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to='group/'),
        ),
    ]
