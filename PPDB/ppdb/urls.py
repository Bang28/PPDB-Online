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
    # data nilai
    listNilaiRaport,
    rekapNilaiPeserta,
    # prestasi
    listPrestasiPeserta,
    rekapPointPrestasi,
    
    pengaturanPrestasi,
    pengaturanAddPrestasi,
    pengaturanEditPrestasi,
    pengaturanDeletePrestasi,
    detailPrestasi,
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
    # prestasi
    prestasiPeserta,
    createPrestasi,
    deletePrestasi,
)

app_name = "ppdb"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('', index, name="index"),
    path('pendaftar/', pendaftar, name="pendaftar"),
    
    # ====== PATH TO BACKEND ======|
    path('dashboard/', dashboard, name="dashboard"),

    # ****Tahun Ajaran****
    path('pengaturan/periode_ppdb/', tahunAjaran, name="periode-ppdb"),    
    path('pengaturan/tambah_periode/', tambahPeriode, name="tambah-periode"),
    path('pengaturan/edit_periode/<periode_id>', editPeriode, name="edit-periode"),
    path('pengaturan/hapus_periode_ppdb/<periode_id>', hapusDataPPDB, name="hapus-periode-ppdb"),

    # ****Peserta PPDB****
    path('data_peserta/list_peserta/', dataPendaftar, name="data-pendaftar"),
    path('data-peserta/peserta_diverfikasi/', dataDiterima, name="data-diterima"),
    path('data_peserta/detail_peserta/<id_peserta>', viewData, name="view-data"),
    path('data_peserta/hapus_peserta/<id>', hapusData, name="hapus-data"),
    path('data_peserta/verifikasi_peserta/', verifikasiSiswa, name="verif"),
    path('data_peserta/email', email, name="email"),
    path('data_peserta/pdf/<id_peserta>', exportPDF, name="pdf"),

    # ****Nilai Peserta****
    path('data_nilai/list_nilai_raport', listNilaiRaport, name="nilai-raport"),
    path('data_nilai/rekap_point_prestasi', rekapPointPrestasi, name="rekap-point"),
    path('data_nilai/rekap_nilai_peserta', rekapNilaiPeserta, name="rekap-nilai"),

    # ***Prestasi Dash Admin***
    path('data_peserta/list_prestasi_peserta', listPrestasiPeserta, name="list-prestasi-peserta"),
    path('data_peserta/detail_prestasi_peserta/<id>', detailPrestasi, name="detail-prestasi"),

    path('pengaturan/prestasi', pengaturanPrestasi, name="pengaturan-prestasi"),
    path('pengaturan/add_prestasi', pengaturanAddPrestasi, name="pengaturan-add-prestasi"),
    path('pengaturan/edit_prestasi/<id_prestasi>', pengaturanEditPrestasi, name="pengaturan-edit-prestasi"),
    path('pengaturan/delete_prestasi/<id_prestasi>', pengaturanDeletePrestasi, name="pengaturan-delete-prestasi"),

    # ***Prestasi Dash Peserta***
    path('peserta/prestasi_peserta/<pk>', prestasiPeserta, name="prestasi-peserta"),
    path('peserta/create_prestasi', createPrestasi, name="create-prestasi"),
    path('peserta/delete_prestasi/<id>', deletePrestasi, name="delete-prestasi"),

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