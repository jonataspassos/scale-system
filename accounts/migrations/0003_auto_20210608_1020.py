# Generated by Django 3.2 on 2021-06-08 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id_telegram',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name_telegram',
        ),
        migrations.RemoveField(
            model_name='user',
            name='telefone',
        ),
    ]
