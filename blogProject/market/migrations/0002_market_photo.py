# Generated by Django 2.2.3 on 2019-08-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='photo',
            field=models.ImageField(default='/', upload_to='upload2/'),
        ),
    ]
