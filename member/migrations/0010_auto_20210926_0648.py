# Generated by Django 3.2.6 on 2021-09-26 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_alter_visited_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visited',
            name='user',
        ),
        migrations.AddField(
            model_name='visited',
            name='member_id',
            field=models.ForeignKey(db_column='member_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='visited',
            name='id',
            field=models.BigAutoField(help_text='Visited_id', primary_key=True, serialize=False),
        ),
    ]
