# Generated by Django 2.0.1 on 2019-10-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage', '0007_auto_20191015_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(null=True),
        ),
    ]
