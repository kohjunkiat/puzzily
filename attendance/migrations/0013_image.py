# Generated by Django 2.0.6 on 2018-06-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]