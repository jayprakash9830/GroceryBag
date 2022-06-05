from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signUp,name='signup'),
    path('login',views.logIn,name="login"),
    path('logout',views.logOut,name="logout"),
    path('additem',views.addItem,name="additem"),
    path('filter',views.filter,name='filter'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name="update"),
    path('update/additem',views.finalupdate,name="finalupdate")
]
