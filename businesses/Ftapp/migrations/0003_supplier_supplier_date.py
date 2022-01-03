# Generated by Django 2.2 on 2021-04-29 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ftapp', '0002_remove_supplier_supplier_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='supplier_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='合作时间'),
        ),
    ]
