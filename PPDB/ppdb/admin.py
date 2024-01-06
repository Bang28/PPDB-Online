from django.contrib import admin
from django.urls import reverse
from . models import TahunAjaran, Formulir, DataAyah, DataIbu, DataWali, Berkas
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(TahunAjaran)
class TahunAjaranAdmin(admin.ModelAdmin):
    list_display = [
        'tahun_ajaran',
        'status',
        'tanggal_mulai',
        'tanggal_selesai',
        ]
    
    
class DataAyahAdmin(admin.StackedInline):
    model = DataAyah

class DataIbuAdmin(admin.StackedInline):
    model = DataIbu

class DataWaliAdmin(admin.StackedInline):
    model = DataWali

class BerkasAdmin(admin.StackedInline):
    model = Berkas
    
    
@admin.register(Formulir)
class FormulirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('foto_peserta', 'nama', 'no_pendaftaran', 'nisn', 'status', 'keterangan', '_')
    readonly_fields = ['no_pendaftaran', 'tgl_daftar']
    radio_fields = {'jenis_kelamin': admin.VERTICAL}
    search_fields = ('nama', 'nisn')
    list_filter = ["verifikasi", "thn_ajaran"]
    list_per_page = (4)

    inlines = [
        DataAyahAdmin,
        DataIbuAdmin,
        DataWaliAdmin,
        BerkasAdmin,
    ]

    def _(self, obj):
        '''fungsi untuk membuat icon'''
        if obj.verifikasi == 'Diterima':
            return True
        elif obj.verifikasi == 'Pending':
            return None
        else:
            return False
    _.boolean = True

    def keterangan(self, obj):
        '''fungsi untuk memberi warna pada teks'''
        if obj.verifikasi == "Diterima":
            color = '#28a745'
        elif obj.verifikasi == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.verifikasi))    
    keterangan.allow_tags =True

