# Generated by Django 4.0.2 on 2022-11-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_user_groups_remove_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, default=None, max_length=7, null=True),
        ),
    ]