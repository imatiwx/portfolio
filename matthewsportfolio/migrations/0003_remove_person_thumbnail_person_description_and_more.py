# Generated by Django 4.0 on 2021-12-13 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matthewsportfolio', '0002_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.CharField(default="I do a lot of crazy stuff with people's money!", max_length=400),
        ),
        migrations.AddField(
            model_name='person',
            name='headline',
            field=models.CharField(default='portfolio Manager', max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(default='static/images/IMG_1303.jpg', null=True, upload_to=''),
        ),
    ]
