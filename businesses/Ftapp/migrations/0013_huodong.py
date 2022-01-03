# Generated by Django 2.2 on 2021-05-10 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ftapp', '0012_supplier_goods_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='HuoDong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('huodong_name', models.CharField(max_length=20)),
                ('huodong_remark', models.TextField(verbose_name='活动详情')),
                ('huodong_img', models.ImageField(upload_to='', verbose_name='活动图片')),
            ],
        ),
    ]
