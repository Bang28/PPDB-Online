from django.db import models
import os
import datetime
from django.utils.html import mark_safe
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


def file_size(value):
    '''fungsi mengatur limit ukuran file yg diupload'''
    limit = 5242880 
    if value.size > limit:
        raise ValidationError('Maksimal ukuran file hanya 5MB')
    

def file_extension(value):
    '''fungsi mengatur ekstensi file yang diizinkan'''
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.png', '.jpg']
    if not ext in valid_extensions:
        raise ValidationError('File tidak didukung, silahkan upload file berupa gambar(png/jpg) atau pdf.')


# Create your models here.
class TahunAjaran(models.Model):
    STATUS_CHOICES = (
        ('', 'Status PPDB'),
        ('Dibuka', 'Dibuka'),
        ('Ditutup', 'Ditutup'),
    )

    id_thn_ajaran   = models.SmallAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    tahun_ajaran    = models.CharField(max_length=20) 
    status          = models.CharField(max_length=10, choices=STATUS_CHOICES)   
    tanggal_mulai   = models.DateField()
    tanggal_selesai = models.DateField()

    def __str__(self):
        return self.tahun_ajaran

    class Meta:
        verbose_name_plural = "Tahun Ajaran"


class Peserta(models.Model):    
    # enum
    STATUS = (
        ('Siswa Baru', 'Siswa Baru'),
        ('Pindahan', 'Pindahan'),
    )
    JENIS_KELAMIN = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )
    AGAMA = (
        ('','Pilih agama'),
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
        ('Kong Hu Cu', 'Kong Hu Cu'),
    )
    PEKERJAAN = (
        ('', 'Pekerjaan'),
        ('Tidak Bekerja', 'Tidak Bekerja'),
        ('Pensiunan', 'Pensiunan'),
        ('PNS', 'PNS'),
        ('TNI/POLRI', 'TNI/POLRI'),
        ('Guru/Dosen', 'Guru/Dosen'),
        ('Pegawai Swasta', 'Pegawai Swasta'),
        ('wiraswasta', 'Wiraswasta'),
        ('Pengacara/Jaksa/Hakim/Notaris', 'Pengacara/Jaksa/Hakim/Notaris'),
        ('Seniman/Pelukis/Artis/Sejenis', 'Seniman/Pelukis/Artis/Sejenis'),
        ('Dokter/Bidan/Perawat', 'Dokter/Bidan/Perawat'),
        ('Pilot/Pramugara', 'Pilot/Pramugara'),
        ('Pedagang', 'Pedagang'),
        ('Petani/Peternak', 'Petani/Peternak'),
        ('Nelayan', 'Nelayan'),
        ('Buruh(Tani/Pabrik/Bangunan)', 'Buruh(Tani/Pabrik/Bangunan)'),
        ('Sopir/Masinis/Kondektur', 'Sopir/Masinis/Kondektur'),
        ('Politikus', 'Politikus'),
        ('lainnya', 'Lainnya')
    )
    KETERANGAN = (
        ('Pending', 'Pending'),
        ('Diterima', 'Diterima'),
        ('Ditolak', 'Ditolak'),
    )
    id_peserta              = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    no_pendaftaran          = models.CharField('No Pendaftaran', max_length=12, unique=True, blank=True, editable=False)
    status                  = models.CharField('Status', max_length=10, choices=STATUS, default=1)
    nama                    = models.CharField('Nama Lengkap', max_length=55)
    tempat_lahir            = models.CharField('Tempat Lahir', max_length=30)
    tgl_lahir               = models.DateField('Tanggal Lahir')
    agama                   = models.CharField('Agama', max_length=10, choices=AGAMA)
    asal_sekolah            = models.CharField('Asal Sekolah', max_length=60)
    jenis_kelamin           = models.CharField('Jenis Kelamin', max_length=15, choices=JENIS_KELAMIN, default="")
    anak_ke                 = models.CharField('Anak Ke', max_length=2, null=True, blank=True)
    tlp_peserta             = models.CharField('No Telp/Wa Peserta', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    alamat                  = models.TextField('Alamat')
    verifikasi              = models.CharField('Status Pendaftaran', max_length=10, null=True, choices=KETERANGAN, default="Pending")
    tgl_daftar              = models.DateTimeField('Tanggal Daftar', auto_now_add=True, null=True, blank=True, editable=False)
    nama_ayah               = models.CharField('Nama Lengkap Ayah', max_length=30, null=True, blank=True)
    pekerjaan_ayah          = models.CharField('Pekerjaan Ayah', max_length=50, choices=PEKERJAAN, null=True, blank=True)
    nama_ibu                = models.CharField('Nama Lengkap Ibu', max_length=30, null=True, blank=True)
    pekerjaan_ibu           = models.CharField('Pekerjaan Ibu', max_length=30, choices=PEKERJAAN, null=True, blank=True)
    tlp_ortu                = models.CharField('No Telp/Wa Orang Tua', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    nama_wali               = models.CharField('Nama Wali', max_length=30, null=True, blank=True)
    pekerjaan_wali          = models.CharField('Pekerjaan Wali', max_length=30, choices=PEKERJAAN, null=True, blank=True)
    tlp_wali                = models.CharField('No Telp/Wa Wali', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')

    # kata kunci asing
    nisn                    = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, verbose_name="NISN", related_name='siswa')
    thn_ajaran              = models.ForeignKey(TahunAjaran, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Tahun Ajaran") # M - 1
        
    # preview image/file
    def foto_peserta(self):
        try:
            return mark_safe(f'<img src = "{self.foto.url}" width = "75"/>')
        except:
            pass
    
    def save(self):
        '''fungsi untuk membuat no pendaftaran otomatis'''
        if not self.no_pendaftaran and self.pk is None:
            last_daftar = Peserta.objects.all().order_by("-pk").first()
            year = datetime.date.today().year
            last_pk = 0
            if last_daftar:
                last_pk = last_daftar.pk
        
            self.no_pendaftaran = "PPDB-" + str(year) + str(last_pk+1).zfill(3)
        super(Peserta, self).save()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Peserta PPDB"


class NilaiRaport(models.Model):
    id_nilai_raport = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    smt_1           = models.FloatField('Semester 1')
    smt_2           = models.FloatField('Semester 2')
    smt_3           = models.FloatField('Semester 3')
    smt_4           = models.FloatField('Semester 4')
    smt_5           = models.FloatField('Semester 5')

    # kata kunci asing
    peserta         = models.OneToOneField(Peserta, on_delete=models.CASCADE, null=True, blank=True, related_name='raport')

    class Meta:
        verbose_name_plural = "Nilai Raport Peserta"


class Prestasi(models.Model):
    id_prestasi     = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    tingkat         = models.CharField('Tingkat', max_length=255, blank=True, null=True)
    kategori        = models.CharField('Kategori', max_length=255, blank=True, null=True)
    juara           = models.CharField('Juara', max_length=255, blank=True, null=True)
    skor_prestasi   = models.FloatField('Skor Prestasi', max_length=255, blank=True, null=True)

    # kata kunci asing
    peserta         = models.ManyToManyField(Peserta, blank=True, related_name='prestasi')

    class Meta:
        verbose_name_plural = "Kategori Prestasi"

class Berkas(models.Model):
    # manage upload + rename file berkas
    def file_kk(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.peserta.no_pendaftaran, instance.peserta.nisn, ext)
        return os.path.join('peserta/berkas/kk', filename)
    def file_akta(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.peserta.no_pendaftaran, instance.peserta.nisn, ext)
        return os.path.join('peserta/berkas/akta', filename)
    def file_raport(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.peserta.no_pendaftaran, instance.peserta.nisn, ext)
        return os.path.join('peserta/berkas/raport', filename)
    def file_skl(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.peserta.no_pendaftaran, instance.peserta.nisn, ext)
        return os.path.join('peserta/berkas/skl', filename)
    def file_ijazah(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.peserta.no_pendaftaran, instance.peserta.nisn, ext)
        return os.path.join('peserta/berkas/ijazah', filename)
    def file_skhun(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.peserta.no_pendaftaran, instance.peserta.nisn, ext)
        return os.path.join('peserta/berkas/skhun', filename)
    
    id_berkas       = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    file_kk         = models.FileField('Kartu Keluarga', max_length=255, upload_to=file_kk, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_akta       = models.FileField('Akta Kelahiran', max_length=255, upload_to=file_akta, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_raport     = models.FileField('Nilai Raport Terakhir', max_length=255, upload_to=file_raport, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_skl        = models.FileField('Surat Keterangan Lulus', max_length=255, upload_to=file_skl, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_ijazah     = models.FileField('Ijazah Jenjang Sebelumnya', max_length=255, upload_to=file_ijazah, validators=[file_extension, file_size], help_text='(Jika sudah ada). File bisa berupa gambar atau pdf', null=True, blank=True)
    file_skhun      = models.FileField('SKHUN', max_length=255, upload_to=file_skhun, validators=[file_extension, file_size], help_text='(Jika sudah ada). File bisa berupa gambar atau pdf', null=True, blank=True)

    # kata kunci asing
    peserta         = models.OneToOneField(Peserta, on_delete=models.CASCADE, null=True, blank=True, related_name='berkas')

    # preview berkas
    def kk_preview(self):
        return mark_safe(f'<img src = "{self.file_kk.url}" width = "275"/>')
    
    def akte_preview(self):
        return mark_safe(f'<img src = "{self.file_akta.url}" width = "275"/>')
    
    def raport_preview(self):
        return mark_safe(f'<img src = "{self.file_raport.url}" width = "275"/>')
    
    def skl_preview(self):
        return mark_safe(f'<img src = "{self.file_skl.url}" width = "275"/>')
    
    def ijazah_preview(self):
        return mark_safe(f'<img src = "{self.file_ijazah.url}" width = "275"/>')
    
    def skhun_preview(self):
        return mark_safe(f'<img src = "{self.file_skhun.url}" width = "275"/>')

    class Meta:
        verbose_name_plural = "Berkas Siswa"