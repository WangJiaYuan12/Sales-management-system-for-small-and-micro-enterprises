from django.contrib import admin
from .models import *


# Register your models here.


class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


class UserAdmin(admin.ModelAdmin):
    date_hierarchy = 'user_create_date'
    list_display = ('user_name', 'user_create_date')
    list_filter = ['user_create_date']
    search_fields = ['user_id', 'username', ]
    fieldsets = [
        (None, {'fields': ['username', 'userpassword']}),
        ('其他信息',
         {'fields': ['user_name', 'user_number', 'user_brithday', 'user_mail', 'user_sex', 'user_address', 'user_img']})
    ]


admin.site.register(user, UserAdmin)


class GoodsAdmin(admin.ModelAdmin):
    date_hierarchy = 'goods_produceddate'
    list_display = ('goods_name', 'goods_produceddate')
    list_filter = ['goods_produceddate']
    search_fields = ['goods_id', 'goods_xinghao', ]
    fieldsets = [
        (None, {'fields': ['goods_name']}),
        ('其他信息', {
            'fields': [ 'goods_xinghao', 'goods_price', 'goods_inventory', 'goods_produceddate', 'goods_img',
                       'goods_remark', 'fenlei_name']})
    ]


admin.site.register(goods, GoodsAdmin)


class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'order_create_time'
    list_display = ('order_id', 'user_name','order_create_time')
    list_filter = ['order_create_time']
    search_fields = ['order_id', 'user_name', ]
    fieldsets = [
        (None, {'fields': ['goods_name']}),
        ('其他信息', {'fields': ['user_name', 'salesman_name', 'order_salestime', 'order_remark', 'goods_number', ]})
    ]


admin.site.register(order, OrderAdmin)


class SalesmanAdmin(admin.ModelAdmin):
    date_hierarchy = 'salesman_hiredate'
    list_display = ('salesman_id', 'salesman_name')
    list_filter = ['salesman_hiredate']
    search_fields = ['salesman_id', 'salesman_name', ]
    fieldsets = [
        (None, {'fields': ['salesman_name']}),
        ('其他信息', {'fields': ['salesman_number', 'salesman_ordernumber', 'salesman_img', 'salesman_sex']})
    ]


admin.site.register(salesman, SalesmanAdmin)


class SupplierAdmin(admin.ModelAdmin):
    date_hierarchy = 'supplier_date'
    list_display = ('supplier_id', 'supplier_name')
    list_filter = ['supplier_date']
    search_fields = ['salesman_id', 'salesman_name', ]
    fieldsets = [
        (None, {'fields': ['supplier_name']}),
        ('其他信息', {'fields': ['supplier_address', 'supplier_number', 'supplier_date','goods_name']})
    ]


admin.site.register(supplier, SupplierAdmin)


class GoodstypeAdmin(admin.ModelAdmin):
    list_display = ('fenlei_id', 'fenlei_name')
    search_fields = ['fenlei_id', 'fenlei_name', ]
    list_filter = ['fenlei_id']
    fieldsets = [
        (None, {'fields': ['fenlei_name']}),

    ]


admin.site.register(goodstype, GoodstypeAdmin)

class HuoDongAdmin(admin.ModelAdmin):
    list_display = ('huodong_name','huodong_remark')
    list_filter = ['huodong_remark']
    fieldsets = [
        (None, {'fields': ['huodong_name','huodong_remark','huodong_img']})

    ]
admin.site.register(HuoDong, HuoDongAdmin)
admin.site.index_title = '欢迎使用销售管理系统后台'
admin.site.site_title = '后台'
admin.site.site_header = '销售管理系统'
