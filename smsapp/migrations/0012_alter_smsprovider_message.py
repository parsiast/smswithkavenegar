# Generated by Django 5.1.1 on 2024-09-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0011_alter_smsprovider_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsprovider',
            name='message',
            field=models.CharField(blank=True, default='a blanked message', max_length=200),
        ),
    ]
