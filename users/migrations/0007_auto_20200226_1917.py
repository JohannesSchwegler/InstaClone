# Generated by Django 3.0.3 on 2020-02-26 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200226_1914'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together=set(),
        ),
    ]
