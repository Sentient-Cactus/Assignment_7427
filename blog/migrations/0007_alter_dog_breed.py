# Generated by Django 3.2.8 on 2021-11-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_dog_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.CharField(default='Unknown', max_length=150),
        ),
    ]
