# Generated by Django 2.2 on 2021-05-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ftapp', '0006_auto_20210429_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_number',
            field=models.CharField(max_length=11, verbose_name='用户手机号'),
        ),
    ]
