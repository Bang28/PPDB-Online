from django.urls import path
from . views import (
    index, 
    dashboard,
    # formulir,
    tahunAjaran,
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
    email,

    singleForm,
    multiForm,
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('', index, name="index"),
    

    # ====== PATH TO BACKEND ======|
    path('dashboard/', dashboard, name="dashboard"),
    # path('formulir/', formulir, name="form"),
    path('datamaster/<pk>', dataMaster, name="data-master"),

    path('periode_ppdb/', tahunAjaran, name="periode-ppdb"),    
    path('tambah_periode/', tambahPeriode, name="tambah-periode"),
    path('edit_periode/<periode_id>', editPeriode, name="edit-periode"),
    path('hapus_periode_ppdb/<periode_id>', hapusDataPPDB, name="hapus-periode-ppdb"),

    path('data_pendaftar/', dataPendaftar, name="data-pendaftar"),
    path('data_diterima/', dataDiterima, name="data-diterima"),
    path('lihat_data/<id>', viewData, name="view-data"),
    path('hapus_data/<id>', hapusData, name="hapus-data"),
    path('terima_formulir/', terimaForm, name="terima"),
    path('tolak_formulir/', tolakForm, name="tolak"),
    
    path('email', email, name="email"),


    path('data_diri/', singleForm, name="single"),
    path('multi_forms/', multiForm, name="multi"),
]