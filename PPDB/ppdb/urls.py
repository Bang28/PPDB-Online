from django.urls import path
from . views import (
    index, 
    register, 
    login_user, 
    dashboard,
    logout_user,
    formulir,
    datamaster,
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH FRONTEND ======|
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),


    # ====== PATH BACKEND ======|
    path('logout/', logout_user, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('formulir/', formulir, name="form"),
    path('datamaster/<pk>', datamaster, name="data"), #regular expression
]