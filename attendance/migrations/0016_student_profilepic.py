# Generated by Django 2.0.6 on 2018-06-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0015_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profilepic',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]