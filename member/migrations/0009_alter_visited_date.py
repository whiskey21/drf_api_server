# Generated by Django 3.2.6 on 2021-09-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_alter_visited_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visited',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]