from django.urls import path
from . views import (
    index, 
    register, 
    login_user, 
    dashboard,
    logout_user,
    formulir,
    datamaster,
    datapendaftar,
    dataditerima,
    viewdata,
    hapusdata,
    markdata,
    tolak,
    userList,
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
    path('datamaster/<pk>', datamaster, name="data"),
    path('data_pendaftar/', datapendaftar, name="dpendaftar"),
    path('data_diterima/', dataditerima, name="dditerima"),
    path('peserta/<id>', viewdata, name="viewdata"),
    path('hapusdata/<id>', hapusdata, name="hapusdata"),
    path('markformulir/', markdata, name="markdata"),
    path('tolakformulir/', tolak, name="tolak"),

    # path to users
    path('userlist/', userList, name="user-list"),
]