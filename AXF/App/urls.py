from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^home/$', home, name='home'),

    url(r'^market/$', market, name='market'),
    url(r'^marketwithparam/(\d+)/(\d+)/(\d+)/$', market_with_param, name='market_with_param'),


    url(r'^mine/$', mine, name='mine'),

    url(r'^register/$',register,name='rehister'),
    url(r'^registerhandle/$',register_handle,name='register_handle'),
    url(r'^checkusername/$',check_username,name='check_username'),
    url(r"^login/$",login,name='login'),
    url(r"^loginhandle/$",login_handle,name='login_handle'),


    url(r'^cart/$', cart, name='cart'),
    url(r"^addtocart/$",add_to_cart,name='add_to_cart'),

    url(r"^logout/$", logout, name='logout'),

]




