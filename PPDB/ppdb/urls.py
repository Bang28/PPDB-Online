from django.urls import path
from .views.index import (
    index, 
    pendaftar,
    dashboard,
)
from .views.adminViews import (
    # siswa/pendaftar
    dataPendaftar,
    dataDiterima,
    viewData,
    hapusData,
    verifikasiSiswa,
    email,
    exportPDF,
    # tahun ajaran
    tahunAjaran,
    tambahPeriode,
    editPeriode,
    hapusDataPPDB,
)
from .views.pesertaViews import (
    dataDiri,
    orangTua,
    wali,
    berkas,
    # update data
    updateDatadiri,
    updateOrangtua,
    updateWali,
    updateBerkas,
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('', index, name="index"),
    path('pendaftar/', pendaftar, name="pendaftar"),
    
    # ====== PATH TO BACKEND ======|
    path('dashboard/', dashboard, name="dashboard"),

    # ****Tahun Ajaran****
    path('periode_ppdb/', tahunAjaran, name="periode-ppdb"),    
    path('tambah_periode/', tambahPeriode, name="tambah-periode"),
    path('edit_periode/<periode_id>', editPeriode, name="edit-periode"),
    path('hapus_periode_ppdb/<periode_id>', hapusDataPPDB, name="hapus-periode-ppdb"),

    # ****Peserta PPDB****
    path('data_pendaftar/', dataPendaftar, name="data-pendaftar"),
    path('data_diterima/', dataDiterima, name="data-diterima"),
    path('lihat_data/<id_siswa>', viewData, name="view-data"),
    path('hapus_data/<id>', hapusData, name="hapus-data"),
    path('verifikasi_siswa/', verifikasiSiswa, name="verif"),
    path('email', email, name="email"),
    path('pdf/<id_siswa>', exportPDF, name="pdf"),

    # ****Formulir Peserta (create)****
    path('formulir/data_diri', dataDiri, name="data-diri"),
    path('formulir/data_orang_tua', orangTua, name="data-ortu"),
    path('formulir/data_wali', wali, name="data-wali"),
    path('formulir/berkas', berkas, name="data-berkas"),
    # ****Formulir Peserta (UPDATE)****
    path('formulir/<id_siswa>/update_data_diri', updateDatadiri, name="update-data-diri"),
    path('formulir/<id_siswa>/update_data_orang_tua', updateOrangtua, name="update-data-ortu"),
    path('formulir/<id_siswa>/update_data_wali', updateWali, name="update-data-wali"),
    path('formulir/<id_siswa>/update_data_berkas', updateBerkas, name="update-berkas"),
]