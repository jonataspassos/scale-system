# Generated by Django 3.2 on 2021-06-08 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegrambot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegramaccount',
            options={'ordering': ['user', 'id_telegram'], 'verbose_name': 'Telegram Account', 'verbose_name_plural': 'Telegram Accounts'},
        ),
        migrations.RemoveField(
            model_name='telegramaccount',
            name='name_telegram',
        ),
        migrations.RemoveField(
            model_name='telegramaccount',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='verificationcode',
            name='name_telegram',
        ),
        migrations.RemoveField(
            model_name='verificationcode',
            name='telefone',
        ),
    ]
