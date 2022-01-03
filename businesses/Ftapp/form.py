# -*-coding:utf-8-*-
import datetime

from django import forms
from Ftapp import views
from captcha.fields import CaptchaField

class LogoForm(forms.Form):
    username = forms.CharField(label="账号", max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "请输入你的账号", 'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-text', 'placeholder': "请输入你的密码"}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (('male', '男'),('female', '女'),)
    username = forms.CharField(label='账号', min_length=6,max_length=128,error_messages={'min_length':'最少输入6位',"required": "用户名不能为空"}, widget=forms.TextInput(attrs={'class': 'form-control bg-white border rounded-lg','placeholder': "请设置你的账号"}))
    password1 = forms.CharField(label='密码', min_length=6,max_length=256,error_messages={'min_length':'最少输入6位'}, widget=forms.PasswordInput(attrs={'class': 'form-control bg-white border rounded-lg','placeholder': "请设置你的密码"}))
    password2 = forms.CharField(label='确认密码', max_length=256,error_messages={"required": "用户名不能为空"}, widget=forms.PasswordInput(attrs={'class': 'form-control bg-white border rounded-lg','placeholder': "请再次输入你的密码"}))
    user_name = forms.CharField(label='姓名', max_length=128,error_messages={"required": "用户名不能为空"}, widget=forms.TextInput(attrs={'class': 'form-control bg-white border rounded-lg','placeholder': "请输入你的昵称"}))
    email = forms.EmailField(label='邮箱地址',error_messages={"required": "用户名不能为空"}, widget=forms.EmailInput(attrs={'class': 'form-control bg-white border rounded-lg','placeholder': "请输入你的邮箱"}))
    address = forms.CharField(label='收货地址', max_length=128,error_messages={"required": "用户名不能为空"}, widget=forms.TextInput(attrs={'class': 'form-control bg-white border rounded-lg ','placeholder': "请输入你的收货地址"}))
    numbers = forms.CharField(label='手机号',error_messages={'required':'标题不为空','min_length':'请输入11位手机号','max_length':'请输入11位手机号'}, widget=forms.TextInput(attrs={'class': 'form-control bg-white border rounded-lg ','placeholder': "请输入你的手机号"}))
    brithday = forms.CharField(label='生日',error_messages={"required": "用户名不能为空"}, widget=forms.TextInput(attrs={'class': 'form-control bg-white border rounded-lg ','placeholder': "请输入你的生日",'type':'date'}) )
    img = forms.ImageField(label='图片',)
    captcha = CaptchaField(label='验证码')
    sex = forms.ChoiceField(label='性别', choices=gender)

class AmendForm(forms.Form):
    user_name = forms.CharField(required=False,label='姓名', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border rounded-lg', 'placeholder': "输入重新设置的昵称"}))
    gender = (('male', '男'), ('female', '女'),)
    username = forms.CharField(required=False,label='账号', min_length=6, max_length=128, error_messages={'min_length': '最少输入6位'},
                               widget=forms.TextInput(attrs={'class': 'form-control bg-white border rounded-lg',
                                                             'placeholder': "输入重新设置的账号"}))
    password1 = forms.CharField(required=False,label='密码', min_length=6, max_length=256, error_messages={'min_length': '最少输入6位'},
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-white border rounded-lg',
                                                                  'placeholder': "输入重新设置的密码"}))
    password2 = forms.CharField(required=False,label='确认密码', max_length=256, widget=forms.PasswordInput(
        attrs={'class': 'form-control bg-white border rounded-lg', 'placeholder': "请再次输入你的密码"}))

    email = forms.EmailField(required=False,label='邮箱地址', widget=forms.EmailInput(
        attrs={'class': 'form-control bg-white border rounded-lg', 'placeholder': "输入重新设置的邮箱"}))
    address = forms.CharField(required=False,label='收货地址', max_length=128, widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border rounded-lg ', 'placeholder': "输入重新设置的地址"}))
    numbers = forms.CharField(required=False,label='手机号', error_messages={'required': '标题不为空', 'min_length': '请输入11位手机号',
                                                           'max_length': '请输入11位手机号'}, widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border rounded-lg ', 'placeholder': "输入重新设置的手机号"}))
    brithday = forms.CharField(required=False,label='生日', widget=forms.TextInput(
        attrs={'class': 'form-control bg-white border rounded-lg ', 'placeholder': "输入重新设置的生日",'type':'date'}))
    img = forms.ImageField(required=False,label='图片', )
    sex = forms.ChoiceField(required=False,label='性别', choices=gender)