# Generated by Django 4.0.2 on 2022-02-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_added',
            field=models.DateField(),
        ),
    ]