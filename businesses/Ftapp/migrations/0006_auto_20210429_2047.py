# Generated by Django 2.2 on 2021-04-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ftapp', '0005_remove_order_goods_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='fenlei',
            new_name='fenlei_name',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='订单编号'),
        ),
    ]
