# Generated by Django 2.2 on 2020-07-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0011_auto_20200704_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, to='feed.Profile'),
        ),
    ]
