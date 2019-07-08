from django.conf.urls import url
from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt



# SET THE NAMESPACE!
app_name = 'chatapp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('user_login/', csrf_exempt(views.user_login), name='user_login'),
    path('register/',views.registration_view, name='register'),

    # path("book/", views.book, name="book"),
    # path("", views.index, name="index"),


    # path('',views.index,name='index'),
    ]