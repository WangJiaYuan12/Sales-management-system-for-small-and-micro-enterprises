from django.shortcuts import render, redirect
from .models import *
from .form import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os.path
from django.db.models import Q

# Create your views here.
def index(request, *args, **kwargs):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        huodong = HuoDong.objects.order_by('id')
        gg = goods.objects.order_by('-goods_id')[:13]
        gg1 = goods.objects.all()
        tp = goodstype.objects.all()
        order_number = order.objects.all()
        salesman_list = salesman.objects.all()
        a=1
        c=0
        b = 0
        us1 = request.session['user_id']
        us = user.objects.order_by('-user_id')[:13]
        for i in salesman_list:  # 计算销售员业绩
            for a in order_number:
                if i.salesman_id == a.salesman_name_id:
                    b += 1
            i.salesman_ordernumber = b
            i.save()
        salesman_rank = salesman.objects.order_by('-salesman_ordernumber')[:13]
        gd = goods.objects.order_by('-goods_id')[:5]  # 按照id倒叙从数据库取出数据，限制五条
        us1 = request.session['user_id']  # 取出对话信息供路由使用
        many = user.objects.order_by('-user_id')[:1]
        return render(request, 'index.html', locals())


def Showorder(request):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        order_all = order.objects.all()
        search_word = request.GET.get('search', '')

        if search_word:
            search_order = order.objects.filter(pk=search_word)
            paginator = Paginator(search_order, 15)
            pages = request.GET.get('page')
            try:
                cons = paginator.page(pages)
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])
            except PageNotAnInteger:
                cons = paginator.page(1)
            return render(request, 'order.html', locals())
        else:
            paginator = Paginator(order_all, 15)
            pages = request.GET.get('page')
            try:
                cons = paginator.page(pages)
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])
            except PageNotAnInteger:
                cons = paginator.page(1)
            return render(request, 'order.html', locals())


def Showsalesman(request):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        salesman_all = salesman.objects.all()
        search_word = request.GET.get('search', '')

        if search_word:
            search_salesman  = salesman.objects.filter(salesman_name=search_word )  # 设置搜索条件
            paginator = Paginator(search_salesman, 15)  # 设置一页多少跳记录
            pages = request.GET.get('page')  # 取得当前页数
            try:
                cons = paginator.page(pages)  # 当前页数的内容赋值给cons
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])  # 当页面数不为int型跳转到最后一页
            except PageNotAnInteger:  # 当页面数超过总页数跳转到最后一页
                cons = paginator.page(1)
            return render(request, 'salesman.html', locals())
        else:
            paginator = Paginator(salesman_all, 15)
            pages = request.GET.get('page')
            try:
                cons = paginator.page(pages)
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])
            except PageNotAnInteger:
                cons = paginator.page(1)
            return render(request, 'salesman.html', locals())


def Showsupplier(request):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        supplier_all = supplier.objects.all()
        search_word = request.GET.get('search', '')

        if search_word:
            search_supplier = salesman.objects.filter(salesman_name=search_word)  # 设置搜索条件
            paginator = Paginator(search_supplier, 15)  # 设置一页多少跳记录
            pages = request.GET.get('page')  # 取得当前页数
            try:
                cons = paginator.page(pages)  # 当前页数的内容赋值给cons
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])  # 当页面数不为int型跳转到最后一页
            except PageNotAnInteger:  # 当页面数超过总页数跳转到最后一页
                cons = paginator.page(1)
            return render(request, 'supplier.html', locals())

        else:
            paginator = Paginator(supplier_all, 15)
            pages = request.GET.get('page')
            try:
                cons = paginator.page(pages)
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])
            except PageNotAnInteger:
                cons = paginator.page(1)
            return render(request, 'supplier.html', locals())



def Showgoods(request):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        gd = goods.objects.all()
        search_word = request.GET.get('search', '')
        if search_word:
            search_goods = goods.objects.filter(goods_name__contains=search_word)  # 设置搜索条件
            paginator = Paginator(search_goods, 15)
            pages = request.GET.get('page')
            try:
                cons = paginator.page(pages)
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])
            except PageNotAnInteger:
                cons = paginator.page(1)
            return render(request, 'goods.html', locals())
        else:
            paginator = Paginator(gd, 15)
            pages = request.GET.get('page')
            try:
                cons = paginator.page(pages)
            except EmptyPage:
                cons = paginator.page([paginator.num_pages])
            except PageNotAnInteger:
                cons = paginator.page(1)
            return render(request, 'goods.html', locals())


def denglu(request):  # 登录功能
    if request.session.get('is_login', None):
        return redirect('/')
    else:
        if request.method == "POST":  # 检测是否是post提交
            logo_form = LogoForm(request.POST)
            message = '请检查填写的内容'
            if logo_form.is_valid():  # 判断表格是否为空
                username1 = logo_form.cleaned_data.get('username')
                password1 = logo_form.cleaned_data.get('password')
                try:
                    user1 = user.objects.get(username=username1)  # 账号校验
                except:
                    message = '用户不存在或账号输入错误'
                    return render(request, 'logo.html', locals())
                if user1.userpassword == password1:  # 账密码校验

                    request.session['is_login'] = True  # 将信息传送给django的会话模块，记录登录信息。
                    request.session['user_id'] = user1.username
                    request.session['user_name'] = user1.user_name

                    return redirect('/')
                else:
                    return render(request, 'logo.html', locals())  # 密码不正确跳转到登陆页面

            else:
                return render(request, 'logo.html', locals())
        else:
            logo_form = LogoForm
            return render(request, 'logo.html', locals())


def logout(request):  # 注销功能
    if not request.session.get('is_login', None):  # 检测用户是否已经登陆
        return redirect('/')  # 重定向首页

    us2 = request.session['user_id']
    request.session.flush()
    return redirect("/logo/")


def file_extension(path):
    return os.path.splitext(path)[1]


def zhuce(request):  # 注册功能
    if request.session.get('is_login', None):  # 检测用户是否已经登陆
        return redirect('/')  # 重定向首页

    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():  # 获取前端输入的数据
            user_name = register_form.cleaned_data.get('user_name')
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            address = register_form.cleaned_data.get('address')
            numbers = register_form.cleaned_data.get('numbers')
            brithday = register_form.cleaned_data.get('brithday')
            sex = register_form.cleaned_data.get('sex')
            img = register_form.cleaned_data.get('img')
            img.name = username + file_extension(str(img.name))
            if password1 != password2:  # 检测密码是否相同
                message = '两次输入的密码不同！'
                return render(request, 'register.html', locals())
            else:
                same_name_user = user.objects.filter(username=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'register.html', locals())

                same_email_user = user.objects.filter(user_mail=email)
                if same_email_user:  # 检测邮箱是否被注册
                    message = '该邮箱已经被注册了！'
                    return render(request, 'register.html', locals())
                if not numbers:  # 检测手机号码是否输入
                    message = '手机号码未输入'
                    return render(request, 'register.html', locals())
                new_user = user()  # 将信息存入数据库
                new_user.user_name = user_name
                new_user.username = username
                new_user.userpassword = password1
                new_user.user_number = numbers
                new_user.user_mail = email
                new_user.user_address = address
                new_user.user_sex = sex
                new_user.user_brithday = brithday
                new_user.user_img = img
                new_user.save()
                return redirect('/logo/')
        else:
            return render(request, 'register.html', locals())
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def ShowAmend(request, us1):
    if not request.session.get('is_login', None):  # 检测用户是否已经登陆
        return redirect('/')  # 重定向首页
    user_form = AmendForm(request.POST, request.FILES)  # 获得form信息
    if request.method == 'POST':

        if user_form.is_valid():
            user_name = user_form.cleaned_data.get('user_name')
            username = user_form.cleaned_data.get('username')
            password1 = user_form.cleaned_data.get('password1')
            password2 = user_form.cleaned_data.get('password2')
            email = user_form.cleaned_data.get('email')
            address = user_form.cleaned_data.get('address')
            numbers = user_form.cleaned_data.get('numbers')
            brithday = user_form.cleaned_data.get('brithday')
            sex = user_form.cleaned_data.get('sex')
            img = user_form.cleaned_data.get('img')
            new_user = user.objects.get(username=us1)
            if user_name:
                new_user.user_name = user_name
            if username:  # 如果对账号进行修改
                same_name_user = user.objects.filter(username=username)
                if same_name_user:
                    message = '用户已存在'
                    return render(request, 'amend.html', locals())
                else:
                    new_user.username = username
            if password1:
                if password1 != password2:  # 检测密码是否相同
                    message = '两次输入的密码不同！'
                    return render(request, 'amend.html', locals())
                else:
                    new_user.userpassword = password1
            if email:
                same_name_email = user.objects.filter(user_mail=email)
                if same_name_email:
                    message = '邮箱已注册'
                    return render(request, 'amend.html', locals())
                else:
                    new_user.user_mail = email
            if address:
                new_user.user_address = address
            if numbers:
                new_user.user_number = numbers
            if brithday:
                new_user.user_brithday = brithday
            if sex:
                new_user.user_sex = sex
            if img:
                img.name = str(new_user.username) + str(file_extension(str(img.name)))
                new_user.user_img = img
            new_user.save()
            us1 = username
            us2 = request.session['user_id']
            request.session.flush()
            return redirect("/logo/")

        else:
            message = '未获得信息'
            return render(request, 'amend.html', locals())
    return render(request, 'amend.html', locals())


def ShoworderDetail(request, order_id):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        order_detail = order.objects.get(order_id=order_id)

        return render(request, 'orderDetail.html', locals())


def ShowgoodsDetail(request, goods_id):
    if not request.session.get('is_login', None):
        return redirect('/logo/')
    else:
        goods_detail = goods.objects.get(goods_id=goods_id)

        return render(request, 'goodsDetail.html', locals())
