# Generated by Django 2.2.6 on 2019-10-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to='accounts/Profile_Pictures'),
        ),
    ]
