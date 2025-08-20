from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.Register,name='register'),
    path('login/',views.login_view,name='login'),
    path('home/',views.home,name='home'),  
    path('logout/',views.logout_view,name = 'logout'),
    path('join/',views.join,name='join_chatroom'),
    path('chat/<str:room_name>/',views.chatroom,name='chatroom'),
    path('delete/<int:chat_id>/',views.delete,name='delete'),
    path('join/again/<int:roomID>/',views.join_again,name='join_again'),
    path('',views.index,name='index'),

]