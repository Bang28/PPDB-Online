from django.urls import path
from . views import (
    index, 
    register, 
    loginUser, 
    dashboard,
    logoutUser,
    formulir,
    pengaturanPPDB,
    dataMaster,
    dataPendaftar,
    dataDiterima,
    viewData,
    hapusData,
    terimaForm,
    tolakForm,
    userAll,
    email,
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH FRONTEND ======|
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', loginUser, name="login"),


    # ====== PATH BACKEND ======|
    path('logout/', logoutUser, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('formulir/', formulir, name="form"),
    path('pengaturan_ppdb/', pengaturanPPDB, name="pengaturan-ppdb"),
    path('datamaster/<pk>', dataMaster, name="data-master"),
    path('data_pendaftar/', dataPendaftar, name="data-pendaftar"),
    path('data_diterima/', dataDiterima, name="data-diterima"),
    path('lihat_data/<id>', viewData, name="view-data"),
    path('hapus_data/<id>', hapusData, name="hapus-data"),
    path('terima_formulir/', terimaForm, name="terima"),
    path('tolak_formulir/', tolakForm, name="tolak"),
    path('pengguna/', userAll, name="user-all"),
    path('email', email, name="email"),
]