# Generated by Django 2.0.6 on 2018-07-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_session_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='attendance_taken',
            field=models.BooleanField(default=False),
        ),
    ]