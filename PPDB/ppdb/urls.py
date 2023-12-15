from django.urls import path
from . views import (
    index, 
    register, 
    loginUser, 
    dashboard,
    logoutUser,
    formulir,
    pengaturanPPDB,
    tambahPeriode,
    editPeriode,
    hapusDataPPDB,
    dataMaster,
    dataPendaftar,
    dataDiterima,
    viewData,
    hapusData,
    terimaForm,
    tolakForm,
    pengguna,
    hapusPengguna,
    tambahPengguna,
    editPengguna,
    email,
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('', index, name="index"),
    path('register/', register, name="register"),
    path('login/', loginUser, name="login"),


    # ====== PATH TO BACKEND ======|
    path('logout/', logoutUser, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('formulir/', formulir, name="form"),
    path('datamaster/<pk>', dataMaster, name="data-master"),

    path('pengaturan_ppdb/', pengaturanPPDB, name="pengaturan-ppdb"),
    path('tambah_periode/', tambahPeriode, name="tambah-periode"),
    path('edit_periode/<periode_id>', editPeriode, name="edit-periode"),
    path('hapus_periode_ppdb/<periode_id>', hapusDataPPDB, name="hapus-periode-ppdb"),

    path('data_pendaftar/', dataPendaftar, name="data-pendaftar"),
    path('data_diterima/', dataDiterima, name="data-diterima"),
    path('lihat_data/<id>', viewData, name="view-data"),
    path('hapus_data/<id>', hapusData, name="hapus-data"),
    path('terima_formulir/', terimaForm, name="terima"),
    path('tolak_formulir/', tolakForm, name="tolak"),

    path('pengguna/', pengguna, name="pengguna"),
    path('tambah_pengguna/', tambahPengguna, name="tambah-pengguna"),
    path('edit_pengguna/<pengguna_id>', editPengguna, name="edit-pengguna"),
    path('hapus_pengguna/<pengguna_id>', hapusPengguna, name="hapus-pengguna"),
    
    path('email', email, name="email"),
]