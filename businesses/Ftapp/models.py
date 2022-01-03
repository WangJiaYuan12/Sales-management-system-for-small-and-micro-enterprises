from django.db import models
import django.utils.timezone as timezone

class user (models.Model):

    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=128 ,verbose_name='用户名称')
    user_number = models.CharField(max_length=11,verbose_name='用户手机号')
    user_brithday = models.DateField(default = timezone.now,verbose_name='用户生日')
    user_create_date = models.DateTimeField(auto_now_add =True,verbose_name='创建时间')
    user_mail = models.EmailField(max_length=256,verbose_name='用户邮箱')
    FEMALE = '女性'
    MALE = '男性'
    USER_SEX = [
        (FEMALE,'女'),
        (MALE,'男')
    ]
    user_sex = models.CharField(
        max_length = 10,
        choices=USER_SEX,
        default= FEMALE,
        verbose_name = '用户性别'
                                    )
    username = models.IntegerField(verbose_name='账号')
    userpassword = models.CharField(max_length=10,verbose_name='密码')
    user_address = models.CharField(max_length=50,verbose_name='地址')
    user_img = models.ImageField(upload_to='',verbose_name='头像')
    def __str__(self):
        return self.user_name

    class Meta:
        # 改变后台列名称
        verbose_name_plural = '用户'
        #改变行名称
        verbose_name='用户'
class salesman (models.Model):
    salesman_id = models.AutoField(primary_key=True,verbose_name='商品名称')
    salesman_name = models.CharField(max_length=10,verbose_name='名字')
    salesman_number = models.BigIntegerField(verbose_name='手机号')
    salesman_hiredate = models.DateField(auto_now_add= True,verbose_name='入职时间')
    salesman_ordernumber = models.IntegerField(verbose_name='销量')
    salesman_img = models.ImageField(upload_to='',verbose_name='销售图片')
    FEMALE = '女性'
    MALE = '男性'
    SALESMAN_SEX = [
        (FEMALE, '女'),
        (MALE, '男')
    ]
    salesman_sex = models.CharField(
        max_length=10,
        choices=SALESMAN_SEX,
        default=FEMALE,
        verbose_name='销售性别'
    )
    def __str__(self):
        return self.salesman_name
    class Meta:
        # 改变后台列名称
        verbose_name_plural = '销售'
        # 改变行名称
        verbose_name = '销售'
class order (models.Model):
    order_id = models.BigAutoField(primary_key=True,verbose_name='订单编号')
    goods_name = models.ForeignKey(
        'goods',
        related_name='goodAname',
        on_delete=models.CASCADE,verbose_name='商品名称'
    )

    user_name = models.ForeignKey(
        'user',
        related_name="userSname",
        on_delete=models.CASCADE,verbose_name='用户名字'
    )
    salesman_name = models.ForeignKey(
        'salesman',
        related_name='nm',
        on_delete=models.CASCADE,verbose_name='销售名字'
    )

    order_create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    order_salestime = models.DateTimeField(verbose_name='销售时间')
    order_salesmoney = models.CharField(max_length=100,verbose_name='销售金额')
    order_remark = models.TextField(verbose_name='订单备注')
    order_remark_img = models.ImageField(upload_to='',verbose_name='备注图片')
    goods_number = models.IntegerField(verbose_name='商品数量')
    def __int__(self):
        return self.order_id
    def __str__(self):
        return self.goods_name
    def __str__(self):
        return self.user_name
    def __str__(self):
        return self.salesman_name
    def __str__(self):
        return self.order_remark
    class Meta:
        # 改变后台列名称
        verbose_name_plural = '订单'
        # 改变行名称
        verbose_name = '订单'

class goods (models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_name = models.CharField(max_length=20,verbose_name='商品名称')
    goods_xinghao = models.CharField(max_length = 20,verbose_name='商品型号')
    goods_price = models.IntegerField(verbose_name='商品价格')
    goods_inventory = models.IntegerField(verbose_name='库存')
    goods_produceddate = models.DateField(default = timezone.now,verbose_name='生产日期')
    goods_img = models.ImageField(upload_to = '',default='1.jpg',height_field = None, width_field = None,verbose_name='商品图片', max_length = 100)
    goods_remark = models.CharField(max_length=255,verbose_name='商品备注')
    fenlei_name = models.ForeignKey(
        'goodstype',
        related_name='type1',
        on_delete=models.CASCADE,verbose_name='商品分类'
    )
    def __int__(self):
        return self.fenlei
    def __int__(self):
        return self.goods_price

    def __str__(self):
        return self.goods_name
    class Meta:
        # 改变后台列名称
        verbose_name_plural = '商品'
        # 改变行名称
        verbose_name = '商品'
class manager (models.Model):
    manager_name = models.CharField(max_length = 20)
    manager_number = models.IntegerField()
class supplier (models.Model):
    supplier_id = models.AutoField(primary_key=True,verbose_name='合作机构编号')
    supplier_name = models.CharField(max_length=20,verbose_name='合作机构名称')
    supplier_address = models.CharField(max_length=20,verbose_name='地址')
    supplier_number = models.BigIntegerField(verbose_name='手机号')
    supplier_date = models.DateField(default = timezone.now,verbose_name='合作时间')
    goods_name =  models.ForeignKey(
        'goods',
        related_name='gm',
        on_delete=models.CASCADE,verbose_name='合作产品'
    )
    class Meta:
        # 改变后台列名称
        verbose_name_plural = '合作商'
        # 改变行名称
        verbose_name = '合作商'
    def __int__(self):
        return self.supplier_id
    def __str__(self):
        return self.supplier_name

class goodstype(models.Model):
    fenlei_id = models.AutoField(primary_key=True,verbose_name='分类编号')
    fenlei = models.SmallIntegerField( )
    fenlei_name = models.CharField(max_length=10,verbose_name='分类名称')
    class Meta:
        # 改变后台列名称
        verbose_name_plural = '商品分类'
        # 改变行名称
        verbose_name = '分类'
    def __str__(self):
        return self.fenlei_name
class HuoDong(models.Model):
    huodong_name = models.CharField(max_length=20,verbose_name='活动名字')
    huodong_remark = models.TextField(verbose_name='活动详情')
    huodong_img = models.ImageField(upload_to='',verbose_name='活动图片')
    class Meta:
        # 改变后台列名称
        verbose_name_plural = '活动展示'
        # 改变行名称
        verbose_name = '活动'
    def __str__(self):
        return self.huodong_name