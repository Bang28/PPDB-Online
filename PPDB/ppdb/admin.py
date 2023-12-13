from django.contrib import admin
from . models import Pengaturan_PPDB, Peserta
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Pengaturan_PPDB)
class PengaturanPPDBAdmin(admin.ModelAdmin):
    list_display = [
        'tahun_ajaran',
        'status',
        'tanggal_mulai',
        'tanggal_selesai',
        ]
    
@admin.register(Peserta)
class PesertaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('foto_peserta', 'nama', 'no_pendaftaran','nisn', 'status', 'keterangan', '_')
    readonly_fields = ['foto_peserta', 'kip_preview', 'pkh_preview', 'kk_preview','akte_preview', 'raport_preview', 'skl_preview', 'ijazah_preview', 'skhun_preview', 'tgl_daftar']
    radio_fields = {'jenis_kelamin': admin.VERTICAL, 'kip': admin.VERTICAL, 'pkh_kks': admin.VERTICAL}
    search_fields = ('nama', 'nisn')
    list_filter = ["Keterangan", "thn_ajaran"]
    list_per_page = (4)
    fields = (
        # peserta didik
        ('nama', 'nisn','thn_ajaran'),
        ('no_hp', 'email'), 
        ('asal_sekolah', 'nik'),
        ('status'),
        ('jenis_kelamin', 'agama'),
        ('tempat_lahir', 'tgl_lahir'),
        ('anak_ke', 'saudara'),
        ('biaya_sekolah', 'status_tinggal_siswa'),
        ( 'alamat_siswa', 'kodepos_siswa'),
        ('transportasi', 'jarak', 'waktu'),
        ('keb_disabilitas'),
        ('pra_sekolah', 'gol_darah'),
        ('kip', 'no_kip'),
        ('pkh_kks', 'no_pkh_kks'),
        ('foto_peserta_didik', 'foto_peserta'),
        # ayah 
        ('nama_ayah', 'nik_ayah'),
        ('status_ayah'),
        ('tempat_lahir_ayah', 'tgl_lahir_ayah'),
        ('pendidikan_ayah', 'pekerjaan_ayah'),
        ('no_hp_ayah', 'penghasilan_ayah'),
        ('status_tmp_tinggal_ayah'),
        # ibu
        ('nama_ibu', 'nik_ibu'),
        ('status_ibu'),
        ('tempat_lahir_ibu', 'tgl_lahir_ibu'),
        ('pendidikan_ibu', 'pekerjaan_ibu'),
        ('no_hp_ibu', 'penghasilan_ibu'),
        # wali
        ('nama_wali', 'nik_wali'),
        ('status_wali'),
        ('tempat_lahir_wali', 'tgl_lahir_wali'),
        ('pendidikan_wali', 'pekerjaan_wali'),
        ('no_hp_wali', 'penghasilan_wali'),
        # dokumen pendukung
        ('file_kip', 'kip_preview'),
        ('file_pkh', 'pkh_preview'),
        ('file_kk', 'kk_preview'),
        ('file_akte', 'akte_preview'),
        ('file_raport', 'raport_preview'),
        ('file_skl', 'skl_preview'),
        ('file_ijazah', 'ijazah_preview'),
        ('file_skhun', 'skhun_preview'),
        ('Keterangan', 'tgl_daftar'),
        'konfirmasi',
    )

    def _(self, obj):
        '''fungsi untuk membuat icon'''
        if obj.Keterangan == 'Diterima':
            return True
        elif obj.Keterangan == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    def keterangan(self, obj):
        '''fungsi untuk memberi warna pada teks'''
        if obj.Keterangan == "Diterima":
            color = '#28a745'
        elif obj.Keterangan == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Keterangan))    
    keterangan.allow_tags =True