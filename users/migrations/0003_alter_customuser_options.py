# Generated by Django 4.2.14 on 2024-08-28 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-date_joined'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]