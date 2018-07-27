from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout




urlpatterns=[
	url(r'^login', login,{'template_name':'recruitmentapp/login.html'}),
  
   url(r'^$',views.hello, name='hello'),
   url(r'^success',views.success, name='success'),
   url(r'^adminpage',views.adminpage, name='adminpage'),
   url(r'^showprofile',views.showprofile, name='showprofile'),
   url(r'^viewprofile',views.viewprofile, name='viewprofile'),
   url(r'^accept',views.accept, name='accept'),
   url(r'^reject',views.reject, name='reject'),
   # url(r'^api-token-auth/', obtain_jwt_token),

]
