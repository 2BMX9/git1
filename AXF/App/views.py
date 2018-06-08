import random
import time
import os
from AXF.settings  import MEDIA_ROOT
import  uuid
import hashlib
from django.shortcuts import render,reverse,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse


# 首页
def home(request):
    #轮播数据
    wheels = MainWheel.objects.all()

    #导航数据
    navs = MainNav.objects.all()

    #必购数据
    mustbuys = MainMustbuy.objects.all()

    #shop数据
    shops = Mainshop.objects.all()
    shop0 = shops.first()
    shop1_2 = shops[1:3]
    shop3_6 = shops[3:7]
    shop7_10 = shops[7:11]

    #主要商品
    mainshows = MainShow.objects.all()

    data = {
        'wheels':wheels,
        'navs' : navs,
        'mustbuys':mustbuys,
        'shop0':shop0,
        'shop1_2':shop1_2,
        'shop3_6':shop3_6,
        'shop7_10':shop7_10,
        'mainshows':mainshows,


    }
    return render(request, 'home/home.html',data)


# 闪购
def market(request):
        return redirect(reverse('App:market_with_param',args=['104749','0','0']))

# 带参数的闪购
def market_with_param(request,typeid,typechildid,sortid):

    # 分类数据
    foodtypes = FoodType.objects.all()
    # 商品数据，根据主分类id进行筛选
    goods_list = Goods.objects.filter(categoryid=typeid)

    #在按照子分类进行筛选
    if typechildid != 0:
        goods_list.filter(childcid=typechildid)



    # 获取当前主分类下的子分类

    childnames = FoodType.objects.filter(typeid=typeid)

    child_type_list = [] #存放子分类的数据
    if childnames.exists():

        childtypes = childnames.first().childtypenames.split('#')
        # print(childtypes) #['全部分类:0']
        for type in childtypes:
            type_list = type.split(':')
            child_type_list.append(type_list)
        # print(child_type_list)



    # 排序规则
    if sortid == '0': #综合排序
        pass;
    if sortid == '1':  # 销量排序
        goods_list = goods_list.order_by('-productnum')
    if sortid == '2':  # 价格降序
        goods_list = goods_list.order_by('-price')
    if sortid == '3':  # 价格升序
        goods_list = goods_list.order_by('price')

    data = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'typeid':typeid,
        'child_type_list':child_type_list,
        'typechildid':typechildid,

    }
    return render(request, 'market/market.html',data)



# 登陆
def  login(request):
  return render(request,'user/login.html')



#登陆的操作
def login_handle(request):

    data = {
        'status':1,
        'msg':'ok'
    }



    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # password = my_md5(password)


        #匹配用户名和秘密
        users = User.objects.filter(name=username,password=password)
        if users.exists():
            #如果登陆成功，进入我的界面
            request.session['userid'] = users.first().id # 保存session
            return redirect(reverse('App:mine'))

        else:
            data['status'] = 0
            data['msg'] = '用户名或密码错误！'
            return render(request,'user/login.html',data)
    data['status'] = -1
    data['msg'] = '请求方式不正确！'
    return render(request,'user/login.html',data)




# 购物车
def cart(request):
    return render(request, 'cart/cart.html')


# 我的
def mine(request):

    data = {
        'name':'',
        'icon':''
    }

    #获取session
    userid = request.session.get('userid','')
    print('userid:',userid)
    if userid:
        user = User.objects.get(id=userid)
        name = user.name  # 用户名
        icon = user.icon  # 获取头像名称
        data['name'] = name
        # print('icon',icon)
        data['icon'] = '/upload/icon/' + icon

    return render(request, 'mine/mine.html',data)

#注册
def register(request):
    return render(request,'user/register.html')

#注册操作
def register_handle(request):

    data = {
        'status':1,
        'msg' : 'ok',

    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon','')


        print('password:',password)

        if len(username)<6:
            data['status'] = 0
            data['msg'] = '输入不合法'
            return render(request,'user/register.html',data)


        #
        # if User.objects.filter(name=username).exists():
        #          return HttpResponse('登录失败')

        #注册
        try:

            user = User()
            user.name = username
            user.password = password
            user.email = email
            #头像
            if icon:

                filename = random_file() + '.png'# icon.name

                user.icon = filename

                filepath =  os.path.join(MEDIA_ROOT,filename)

                with open(filepath,'ab') as  fp:
                    for part in icon.chunks():
                        fp.write(part)
                        fp.flush()


            else:
                user.icon = ''
            user.save()

            # 保存 session
            request.session['userid'] = user.id



            return redirect(reverse('App:mine'))
            # return HttpResponse('登录成功')

        except:
            return redirect(reverse('App:register'))
            # return  HttpResponse('登录失败')

    return redirect(reverse('App:register'))
    # return  HttpResponse('登录失败')

# 获取随即的文件名
def random_file():
   u = str(uuid.uuid4())
   m = hashlib.md5()
   m.update(u.encode('utf-8'))
   return m.hexdigest()


# 退出登陆
def logout(request):
    #删除session
    request.session.flush()
    return redirect(reverse('App:mine'))


#用户名检测
def check_username(request):
    if request.method == "GET":
        username = request.GET.get('username')
        users =  User.objects.filter(name=username)

        # 如果存在
        if users.exists():
            return JsonResponse({'status':0,'msg':'用户已存在'})
        # 如果存不在
        else:
            return JsonResponse({'status':1,'msg':'ok'})

    return JsonResponse({'status':-1,'msg':'请求方式不正取'})



# md5加密
def my_md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()





# 加入购物车
def add_to_cart(request):

    data = {
        'status' : 1,
        'msg' : 'ok'
    }

    # 判断user is login
    userid = request.session.get('userid','')
    if not userid:
        data['status'] = 0
        data['msg'] = '用户未登陆'
    else:
        if request.method == "GET":
            goodsid = request.GET.get("goodsid")
            num = request.GET.get("num")

            # 添加到购物车
            cart = Cart()
            cart.user_id = userid
            cart.goods_id = goodsid
            cart.num = num
            cart.save()
        else:
            data['status'] = -1
            data['msg'] = '请求方式不正确'
            return JsonResponse(data)

    return JsonResponse(data)