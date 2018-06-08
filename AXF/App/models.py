from django.db import models


# 首页
class Main(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=20)

    # 给表明改名字
    class Meta:
        abstract = True # 抽象类，不会生成表
# 首页-轮播
class MainWheel(Main):
     class Meta:
        db_table = 'axf_wheel'

#首页-导航
class MainNav(Main):
    class Meta:
        db_table ="axf_nav"

#首页-必购
class MainMustbuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'



#首页-shop
class Mainshop(Main):
    class Meta:
        db_table = 'axf_shop'


# 商品展示

class MainShow(Main):

    categoryid = models.CharField(max_length=50)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=20)
    marketprice1 =models.CharField(max_length=20)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'




    # 商品类型
class FoodType(models.Model):
        typeid = models.CharField(max_length=20)
        typename = models.CharField(max_length=20)
        childtypenames = models.CharField(max_length=200)
        typesort = models.IntegerField(default=1)

        class Meta:
            db_table = 'axf_foodtypes'



'''
insert into axf_goods(
    productid,productimg,productname,productlongname,
    isxf,pmdesc,specifics,price,marketprice,
    categoryid,childcid,childcidname,dealerid,
    storenums,productnum) 
values(
    "11951","1.jpg","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,
    103541,103543,"膨化食品","4858",200,4);
'''

# 商品
class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=0)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=20)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=20)
    childcid =  models.CharField(max_length=20)
    childcidname = models.CharField(max_length=20)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table= 'axf_goods'



# 用户
class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    icon = models.CharField(max_length=50,null=True,blank=True)
    sex = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)


# 购物车
class Cart(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)


#订单
class Order(models.Model):
    order_id = models.CharField(max_length=50,unique=True)
    order_createtime = models.DateTimeField(auto_now_add=True)
    order_price = models.FloatField()
    # 订单状态:0表示为支付(待付款),1表示已付款(待收货),2表示待评价,3表示交易完成
    order_status = models.CharField(max_length=10,default=0)
    user = models.ForeignKey(User)

#订单中的商品
class OrderGoods(models.Model):
    goods = models.ForeignKey(Goods)
    order = models.ForeignKey(Order)
    num = models.IntegerField(default=1)
    price = models.FloatField()






