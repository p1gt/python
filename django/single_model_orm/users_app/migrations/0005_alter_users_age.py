# Generated by Django 4.2.1 on 2023-06-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_alter_users_age_alter_users_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(),
        ),
    ]