from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path
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
    unduhFile,
    # tahun ajaran
    tahunAjaran,
    tambahPeriode,
    editPeriode,
    hapusDataPPDB,
)
from .views.pesertaViews import (
    peserta,
    nilaiRaport,
    berkas,
    # update data
    updatePeserta,
    updateNilaiRaport,
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
    path('lihat_data/<id_peserta>', viewData, name="view-data"),
    path('hapus_data/<id>', hapusData, name="hapus-data"),
    path('verifikasi_siswa/', verifikasiSiswa, name="verif"),
    path('email', email, name="email"),
    path('pdf/<id_peserta>', exportPDF, name="pdf"),

    # *****Peserta File*****
    # re_path(r'^download/(?P<path>.*)/$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^download/(?P<path>.*)/$', unduhFile, name="unduh"),

    # ****Formulir Peserta (create)****
    path('formulir/form_peserta', peserta, name="data-peserta"),
    path('formulir/form_nilai_raport', nilaiRaport, name="data-nilai"),
    path('formulir/form_berkas', berkas, name="data-berkas"),
    # ****Formulir Peserta (UPDATE)****
    path('formulir/<id_peserta>/update_data_peserta', updatePeserta, name="update-data-peserta"),
    path('formulir/<id_peserta>/update_data_nilai', updateNilaiRaport, name="update-data-nilai"),
    path('formulir/<id_peserta>/update_data_berkas', updateBerkas, name="update-berkas"),
]