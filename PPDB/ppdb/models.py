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


class Siswa(models.Model):
    def image_upload_to(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.no_pendaftaran, instance.nama, ext)
        return os.path.join('siswa/foto siswa', filename)
    
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
    STATUS_TINGGAL = (
        ('', 'Pilih status tinggal'),
        ('Tinggal dengan ORTU/WALI', 'Tinggal dengan ORTU/WALI'),
        ('Ikut Saudara/Kerabat', 'Ikut Saudara/Kerabat'),
        ('Asrama', 'Asrama'),
        ('Kontrak/Kost', 'Kontrak/Kost'),
        ('Panti Asuhan', 'Panti Asuhan'),
        ('lainnya', 'Lainnya'),
    )
    TRANSPOSTASI = (
        ('', 'Pilih transportasi'),
        ('Jalan Kaki', 'Jalan Kaki'),
        ('Sepeda', 'Sepeda'),
        ('Sepeda Motor', 'Sepeda Motor'),
        ('Mobil Pribadi', 'Mobil Pribadi'),
        ('Angkutan Umum', 'Angkutan Umum'),
        ('lainnya', 'Lainnya'),
    )
    BIAYA_SEKOLAH = (
        ('', 'Biaya sekolah'),
        ('Orangtua', 'Orangtua'),
        ('Wali/Orangtua Asuh', 'Wali/Orangtua Asuh'),
        ('Tanggung Sendiri', 'Tanggung Sendiri'),
        ('Lainnya', 'Lainnya'),
    )
    KEBUTUHAN_DISABILITAS = (
        ('', 'Kebutuhan disabilitas'),
        ('Tidak Ada', 'Tidak Ada'),
        ('Tuna Netra', 'Tuna Netra'),
        ('Tuna Rungu', 'Tuna Rungu'),
        ('Tuna Daksa', 'Tuna Daksa'),
        ('Tuna Grahita', 'Tuna Grahita'),
        ('Tuna Laras', 'Tuna Laras'),
        ('Lainnya', 'Lainnya'),
    )
    KETERANGAN = (
        ('Pending', 'Pending'),
        ('Diterima', 'Diterima'),
        ('Ditolak', 'Ditolak'),
    )
    id_siswa                = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    no_pendaftaran          = models.CharField('No Pendaftaran', max_length=12, unique=True, blank=True, editable=False)
    status                  = models.CharField('Status', max_length=10, choices=STATUS, default=1)
    nama                    = models.CharField('Nama Lengkap', max_length=55)
    nik                     = models.CharField('NIK', max_length=16)
    tempat_lahir            = models.CharField('Tempat Lahir', max_length=30)
    tgl_lahir               = models.DateField('Tanggal Lahir')
    agama                   = models.CharField('Agama', max_length=10, choices=AGAMA)
    asal_sekolah            = models.CharField('Asal Sekolah', max_length=60)
    jenis_kelamin           = models.CharField('Jenis Kelamin', max_length=15, choices=JENIS_KELAMIN, default="")
    anak_ke                 = models.CharField('Anak Ke', max_length=2, null=True, blank=True)
    saudara                 = models.CharField('Jumlah Saudara', max_length=2, null=True, blank=True)
    no_hp                   = models.CharField('No Telp/Wa', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    email                   = models.EmailField('Email', help_text='Pastikan email aktif dan dapat dihubungi.')
    status_tinggal          = models.CharField('Status Tinggal', max_length=50, choices=STATUS_TINGGAL)
    alamat                  = models.TextField('Alamat')
    kodepos                 = models.CharField('Kode POS', max_length=6, null=True, blank=True)
    transportasi            = models.CharField('Mode Transportasi', max_length=30, choices=TRANSPOSTASI, null=True, blank=True)
    biaya_sekolah           = models.CharField('Biaya Sekolah', max_length=30, choices=BIAYA_SEKOLAH)
    keb_disabilitas         = models.CharField('Kebutuhan Disabilitas', max_length=20, choices=KEBUTUHAN_DISABILITAS)
    foto                    = models.ImageField('Foto', max_length=255, upload_to=image_upload_to, help_text='foto 3x4 dengan background merah')
    verifikasi              = models.CharField('Status Pendaftaran', max_length=10, null=True, choices=KETERANGAN, default="Pending")
    tgl_daftar              = models.DateTimeField('Tanggal Daftar', auto_now_add=True, null=True, blank=True, editable=False)

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
            last_daftar = Siswa.objects.all().order_by("-pk").first()
            year = datetime.date.today().year
            last_pk = 0
            if last_daftar:
                last_pk = last_daftar.pk
        
            self.no_pendaftaran = "PPDB-" + str(year) + str(last_pk+1).zfill(3)
        super(Siswa, self).save()

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Peserta PPDB"


# enum
STATUS_ORTU = (
    ('', 'Status'),
    ('Masih Hidup', 'Masih Hidup'),
    ('Sudah Meninggal', 'Sudah Meninggal'),
    ('Tidak Diketahui', 'Tidak Diketahui'),
)
PENDIDIKAN_ORTU = (
    ('', 'Pendidikan'),
    ('Tidak Sekolah', 'Tidak Sekolah'),
    ('sd', 'SD/Sederajad'),
    ('smp', 'SMP/Sederajad'),
    ('sma', 'SMA/Sederajad'),
    ('d1', 'D1'),
    ('d2', 'D2'),
    ('d3', 'D3'),
    ('s1', 'D4/S1'),
    ('s2', 'S2'),
    ('s3', 'S3'),
)
PEKERJAAN_ORTU = (
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
PENGHASILAN_ORTU = (
    ('', 'Penghasilan'),
    ('>500k', 'Kurang dari 500.000'),
    ('500-1000k', '500.000-1.000.000'),
    ('1000-2000k', '1.000.000-2.000.000'),
    ('2000-3000k', '2.000.000-3.000.000'),
    ('3000-4000k', '3.000.000-4.000.000'),
    ('3000-4000k', '3.000.000-4.000.000'),
    ('4000-5000k', '4.000.000-5.000.000'),
    ('>5000k', 'Lebih dari 5.000.000'),
)
STATUS_TINGGAL_ORTU = (
    ('', 'Status tinggal'),
    ('Milik Sendiri', 'Milik Sendiri'),
    ('Rumah Orangtua', 'Rumah Orangtua'),
    ('Rumah Saudara/Kerabat', 'Rumah Saudara/Kerabat'),
    ('Rumah Dinas', 'Rumah Dinas'),
    ('Sewa/Kontrak', 'Sewa/Kontrak'),
    ('lainnya', 'Lainnya'),
)


class OrangTua(models.Model):
    id_ortu                 = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    nama_ayah               = models.CharField('Nama Lengkap Ayah', max_length=30, null=True, blank=True)
    status_ayah             = models.CharField('Status Ayah', max_length=30, choices=STATUS_ORTU, null=True, blank=True)
    nik_ayah                = models.CharField('NIK Ayah', max_length=16, null=True, blank=True)
    status_ibu              = models.CharField('Status Ibu', max_length=30, choices=STATUS_ORTU, null=True, blank=True)
    tempat_lahir_ayah       = models.CharField('Tempat Lahir Ayah', max_length=20, null=True, blank=True)
    tgl_lahir_ayah          = models.DateField('Tanggal Lahir Ayah', null=True, blank=True)
    pendidikan_ayah         = models.CharField('Pendidikan Ayah', max_length=25, choices=PENDIDIKAN_ORTU, null=True, blank=True)
    pekerjaan_ayah          = models.CharField('Pekerjaan Ayah', max_length=50, choices=PEKERJAAN_ORTU, null=True, blank=True)
    penghasilan_ayah        = models.CharField('Penghasilan Ayah', max_length=30, choices=PENGHASILAN_ORTU, null=True, blank=True)
    nama_ibu                = models.CharField('Nama Lengkap Ibu', max_length=30, null=True, blank=True)
    status_ibu              = models.CharField('Status Ibu', max_length=30, choices=STATUS_ORTU, null=True, blank=True)
    nik_ibu                 = models.CharField('NIK Ibu', max_length=16,  null=True, blank=True)
    tempat_lahir_ibu        = models.CharField('Tempat Lahir Ibu', max_length=20, null=True, blank=True)
    tgl_lahir_ibu           = models.DateField('Tanggal Lahir Ibu', null=True, blank=True)
    pendidikan_ibu          = models.CharField('Pendidikan Ibu', max_length=25, choices=PENDIDIKAN_ORTU, null=True, blank=True)
    pekerjaan_ibu           = models.CharField('Pekerjaan Ibu', max_length=30, choices=PEKERJAAN_ORTU, null=True, blank=True)
    penghasilan_ibu         = models.CharField('Penghasilan Ibu', max_length=25, choices=PENGHASILAN_ORTU, null=True, blank=True)
    no_hp_ortu              = models.CharField('No Telp/Wa', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    status_tmp_tinggal_ortu = models.CharField('Status Tempat Tinggal Orang Tua', max_length=25, choices=STATUS_TINGGAL_ORTU, null=True, blank=True)

    # kata kunci asing
    siswa                   = models.OneToOneField(Siswa, on_delete=models.CASCADE, null=True, blank=True, related_name='ortu')

    class Meta:
        verbose_name_plural = "Data Ayah Siswa"


class Wali(models.Model):
    STATUS_WALI = (
        ('', 'Status Wali'),
        ('Sama dengan Orangtua', 'Sama dengan Orangtua'),
        ('Lainnya', 'Lainnya')
    )
    id_wali             = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    nama_wali           = models.CharField('Nama Wali', max_length=30, null=True, blank=True)
    status_wali         = models.CharField('Status Wali', max_length=30, choices=STATUS_WALI)
    nik_wali            = models.CharField('NIK Wali', max_length=16, null=True, blank=True)
    tempat_lahir_wali   = models.CharField('Tempat Lahir Wali', max_length=30, null=True, blank=True)
    tgl_lahir_wali      = models.DateField('Tanggal Lahir Wali', null=True, blank=True)
    pendidikan_wali     = models.CharField('Pendidikan Wali', max_length=25, choices=PENDIDIKAN_ORTU, null=True, blank=True)
    pekerjaan_wali      = models.CharField('Pekerjaan Wali', max_length=30, choices=PEKERJAAN_ORTU, null=True, blank=True)
    penghasilan_wali    = models.CharField('Penghasilan Wali', max_length=25, choices=PENGHASILAN_ORTU, null=True, blank=True)
    no_hp_wali          = models.CharField('No Telp/Wa Wali', max_length=15, null=True, blank=True)     

    # kata kunci asing
    siswa               = models.OneToOneField(Siswa, on_delete=models.CASCADE, null=True, blank=True, related_name='wali')

    class Meta:
        verbose_name_plural = "Data Wali Siswa"

class Berkas(models.Model):
    # manage upload + rename file berkas
    def file_kk(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.siswa.no_pendaftaran, instance.siswa.nisn, ext)
        return os.path.join('siswa/berkas/kk', filename)
    def file_akta(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.siswa.no_pendaftaran, instance.siswa.nisn, ext)
        return os.path.join('siswa/berkas/akta', filename)
    def file_raport(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.siswa.no_pendaftaran, instance.siswa.nisn, ext)
        return os.path.join('siswa/berkas/raport', filename)
    def file_skl(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.siswa.no_pendaftaran, instance.siswa.nisn, ext)
        return os.path.join('siswa/berkas/skl', filename)
    def file_ijazah(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.siswa.no_pendaftaran, instance.siswa.nisn, ext)
        return os.path.join('siswa/berkas/ijazah', filename)
    def file_skhun(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % (instance.siswa.no_pendaftaran, instance.siswa.nisn, ext)
        return os.path.join('siswa/berkas/skhun', filename)
    
    id_berkas       = models.BigAutoField(primary_key=True, unique=True, auto_created=True, blank=True)
    file_kk         = models.FileField('Kartu Keluarga', max_length=255, upload_to=file_kk, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_akta       = models.FileField('Akta Kelahiran', max_length=255, upload_to=file_akta, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_raport     = models.FileField('Nilai Raport Terakhir', max_length=255, upload_to=file_raport, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_skl        = models.FileField('Surat Keterangan Lulus', max_length=255, upload_to=file_skl, validators=[file_extension, file_size], help_text='File bisa berupa gambar atau pdf')
    file_ijazah     = models.FileField('Ijazah Jenjang Sebelumnya', max_length=255, upload_to=file_ijazah, validators=[file_extension, file_size], help_text='(Jika sudah ada). File bisa berupa gambar atau pdf', null=True, blank=True)
    file_skhun      = models.FileField('SKHUN', max_length=255, upload_to=file_skhun, validators=[file_extension, file_size], help_text='(Jika sudah ada). File bisa berupa gambar atau pdf', null=True, blank=True)

    # kata kunci asing
    siswa           = models.OneToOneField(Siswa, on_delete=models.CASCADE, null=True, blank=True, related_name='berkas')

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