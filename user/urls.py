from django.urls import path
from .import views


urlpatterns = [
    path('', views.home,name='home'),
    path('explore/',views.explore,name='explore'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    # path('posts/', view    s.posts,name='posts'),
    path('register/',views.register,name='register'),
    path('add/',views.add, name='add'),
    path('submitCity/',views.submitCity,name='submitCity'),
    path('manage/',views.manage,name='manage'),
    path('edit/<cid>',views.edit,name='edit'),

]

#the first parameter the we pass is the name that will be visible on urls container in the top.
#views.<function name that we are mentioning in views.py>
# name='<the name we are menioning in html pages in anchor tag>' generally we mention this in a navbar or a button when we  click on that, it should lead to particular web page. 