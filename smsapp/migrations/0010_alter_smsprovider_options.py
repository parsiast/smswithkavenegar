# Generated by Django 5.1.1 on 2024-09-07 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0009_alter_smsprovider_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='smsprovider',
            options={'ordering': ['created', 'message', 'sender', 'receptor']},
        ),
    ]
