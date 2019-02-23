from django.shortcuts import render, redirect, reverse, HttpResponse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.views.generic import View
import re
from user.models import User, Address
from goods.models import GoodsSKU
from django.conf import settings
from celery_tasks.tasks import send_register_active_email
from django.contrib.auth import authenticate, login ,logout
from utils.mixin import LoginRequiredMixin
from django_redis import get_redis_connection

# Create your views here.
def register_user(request):

    return render(request, 'user/register.html')


class Register_view(View):
    def get(self, request):
        '''访问'''
        return render(request, 'user/register.html')

    def post(self, request):
        '''注册用户'''
        username = request.POST.get("user_name")
        pwd = request.POST.get("pwd")
        email = request.POST.get("email")
        allow = request.POST.get("allow")

        # 判断不为空
        if not all([username, pwd, email]):
            return render(request, 'user/register.html', {"errmsg": "输入信息错误"})
        # 校验电子邮箱
        if not re.match(r"^[0-9a-zA-Z_]{1,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$", email):
            return render(request, 'user/register.html', {"errmsg": "电子邮箱信息错误"})

        if allow != "on":
            return render(request, 'user/register.html', {"errmsg": "请勾选同意协议"})

        # 判断是否用户已经注册
        # User.objects.create_user(username, email, pwd)
        user = User.objects.create_user(username, email, pwd)
        user.is_active = 0
        user.save()

        # 生成激活链接
        ser = Serializer(settings.SECRET_KEY, 7200)
        info = {'confirm' : user.id}
        token = ser.dumps(info)
        token = token.decode('utf8')
        receiver = [user.email]

        # # 发送邮件
        # subject = "天天生鲜欢迎信息"
        # htmlmsg = "<h1>%s,欢迎激活注册会员</h1>请点击下面的链接激活<br/><a href='http://127.0.0.1:8000/user/active/%s'>http://127.0.0.1:8000/user/active/%s</a>" % (user.username, token, token)
        # sender = settings.EMAIL_FROM
        # send_mail(subject, '', sender, receiver, html_message=htmlmsg)
        send_register_active_email.delay(receiver, user.username, token)
        return redirect(reverse('goods:index'))

class Active_view(View):
    """用户激活"""
    def get(self, request, id):
        # 进行解密
        ser = Serializer(settings.SECRET_KEY, 7200)
        try:
            info = ser.loads(id)
            user_id = info["confirm"]
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

            return redirect(reverse("user:login"))
        except SignatureExpired as e:
            return HttpResponse("激活链接失败！")

class Login_view(View):
    """处理登录"""
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        # 校验数据问题
        if not all([username, pwd]):
            return render(request, "user/login.html", {'errmsg': '用户名密码不能为空'})

        # 校验用户名密码
        # User.objects.get(username=username, password=pwd)
        user = authenticate(username=username, password=pwd)
        if user is not None:
            if not user.is_active:
                return render(request, "user/login.html", {'errmsg': '用户未激活'})
            else:
                login(request, user)
                return redirect(reverse("goods:index"))
        else:
            return render(request, "user/login.html", {'errmsg': '用户名密码错误'})

# /user/logout
class Logout_View(View):
    '''退出登录'''
    def get(self, request):
        '''退出登录'''
        # 清除用户的session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('goods:index'))

# /user
class UserInfo_View(LoginRequiredMixin, View):
    '''用户中心-信息页'''
    def get(self, request):
        '''显示'''
        # Django会给request对象添加一个属性request.user
        # 如果用户未登录->user是AnonymousUser类的一个实例对象
        # 如果用户登录->user是User类的一个实例对象
        # request.user.is_authenticated()

        # 获取用户的个人信息
        user = request.user
        address = Address.objects.get_default_address(user)

        # 获取用户的历史浏览记录
        # from redis import StrictRedis
        # sr = StrictRedis(host='172.16.179.130', port='6379', db=9)
        con = get_redis_connection('default')

        history_key = 'history_%d'%user.id

        # 获取用户最新浏览的5个商品的id
        sku_ids = con.lrange(history_key, 0, 4) # [2,3,1]

        # 从数据库中查询用户浏览的商品的具体信息
        # goods_li = GoodsSKU.objects.filter(id__in=sku_ids)
        #
        # goods_res = []
        # for a_id in sku_ids:
        #     for goods in goods_li:
        #         if a_id == goods.id:
        #             goods_res.append(goods)

        # 遍历获取用户浏览的商品信息
        goods_li = []
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_li.append(goods)

        # 组织上下文
        context = {'page':'user',
                   'address':address,
                   'goods_li':goods_li}

        # 除了你给模板文件传递的模板变量之外，django框架会把request.user也传给模板文件
        return render(request, 'user/user_center_info.html', context)


# /user/order
class UserOrder_View(LoginRequiredMixin, View):
    '''用户中心-订单页'''
    def get(self, request):
        '''显示'''
        # 获取用户的订单信息

        return render(request, 'user/user_center_order.html', {'page':'order'})


# /user/address
class Address_View(LoginRequiredMixin, View):
    '''用户中心-地址页'''
    def get(self, request):
        '''显示'''
        # 获取登录用户对应User对象
        user = request.user

        # 获取用户的默认收货地址
        # try:
        #     address = Address.objects.get(user=user, is_default=True) # models.Manager
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None
        address = Address.objects.get_default_address(user)

        # 使用模板
        return render(request, 'user/user_center_site.html', {'page':'address', 'address':address})

    def post(self, request):
        '''地址的添加'''
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        # 校验数据
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg':'数据不完整'})

        # 校验手机号
        if not re.match(r'^1[3|4|5|7|8][0-9]{9}$', phone):
            return render(request, 'user_center_site.html', {'errmsg':'手机格式不正确'})

        # 业务处理：地址添加
        # 如果用户已存在默认收货地址，添加的地址不作为默认收货地址，否则作为默认收货地址
        # 获取登录用户对应User对象
        user = request.user

        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 不存在默认收货地址
        #     address = None

        address = Address.objects.get_default_address(user)

        if address:
            is_default = False
        else:
            is_default = True

        # 添加地址
        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               zip_code=zip_code,
                               phone=phone,
                               is_default=is_default)

        # 返回应答,刷新地址页面
        return redirect(reverse('user:address')) # get请求方式



