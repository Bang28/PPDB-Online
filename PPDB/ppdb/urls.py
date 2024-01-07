from django.urls import path
from .views.index import (
    index, 
    dashboard,
)
from .views.periode import (
    tahunAjaran,
    tambahPeriode,
    editPeriode,
    hapusDataPPDB,
)
from .views.peserta import (
    dataPendaftar,
    dataDiterima,
    viewData,
    hapusData,
    terimaForm,
    tolakForm,
    email,
)
from .views.formulir import (
    dataMaster,
    dataDiri,
    dataAyah,
    dataIbu,
    dataWali,
    berkas
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('', index, name="index"),
    
    # ====== PATH TO BACKEND ======|
    path('dashboard/', dashboard, name="dashboard"),

    # ****Periode****
    path('periode_ppdb/', tahunAjaran, name="periode-ppdb"),    
    path('tambah_periode/', tambahPeriode, name="tambah-periode"),
    path('edit_periode/<periode_id>', editPeriode, name="edit-periode"),
    path('hapus_periode_ppdb/<periode_id>', hapusDataPPDB, name="hapus-periode-ppdb"),

    # ****Peserta****
    path('data_pendaftar/', dataPendaftar, name="data-pendaftar"),
    path('data_diterima/', dataDiterima, name="data-diterima"),
    path('lihat_data/<id>', viewData, name="view-data"),
    path('hapus_data/<id>', hapusData, name="hapus-data"),
    path('terima_formulir/', terimaForm, name="terima"),
    path('tolak_formulir/', tolakForm, name="tolak"),
    path('email', email, name="email"),

    # ****Formulir****
    path('formulir/data_diri', dataDiri, name="data-diri"),
    path('formulir/data_ayah', dataAyah, name="data-ayah"),
    path('formulir/data_ibu', dataIbu, name="data-ibu"),
    path('formulir/data_wali', dataWali, name="data-wali"),
    path('formulir/berkas', berkas, name="data-berkas"),
    path('datamaster/<pk>', dataMaster, name="data-master"),
]