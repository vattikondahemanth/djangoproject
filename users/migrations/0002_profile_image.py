# Generated by Django 2.2b1 on 2019-04-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defualt.jpg', upload_to='profile_pics'),
        ),
    ]
