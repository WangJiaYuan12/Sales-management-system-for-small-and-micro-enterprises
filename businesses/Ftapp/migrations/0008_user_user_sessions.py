# Generated by Django 2.2 on 2021-05-04 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ftapp', '0007_auto_20210503_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_sessions',
            field=models.BooleanField(default=False),
        ),
    ]
