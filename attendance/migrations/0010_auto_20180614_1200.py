# Generated by Django 2.0.6 on 2018-06-14 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_auto_20180614_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='tutorials',
            new_name='tutorial',
        ),
    ]