from django.db import models
from django.utils.text import slugify
import os
import datetime
from django.utils.html import mark_safe
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Pengaturan_PPDB(models.Model):
    tahun_ajaran    = models.CharField(max_length=20) 
    STATUS_CHOICES = (
        ('Dibuka', 'Dibuka'),
        ('Ditutup', 'Ditutup'),
    )
    status          = models.CharField(max_length=10, choices=STATUS_CHOICES)
    tanggal_mulai   = models.DateField()
    tanggal_selesai = models.DateField()

    def __str__(self):
        return self.tahun_ajaran

    class Meta:
        verbose_name_plural = "Pengaturan PPDB"


class Peserta(models.Model):
    def file_upload_to(self, instance=None):
        if instance:
            return os.path.join("Peserta/Berkas Peserta", slugify(self.nisn), instance)
        return None
    
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Peserta/Foto Peserta", slugify(self.nisn), instance)
        return None
    

    # data tuple pendidik
    STATUS_PESERTA_CHOICES = (
        ('Siswa Baru', 'Siswa Baru'),
        ('Pindahan', 'Pindahan'),
    )
    STATUS_WARGA_NEGARA = (
        ('', 'Warga negara'),
        ('WNI', 'WNI'),
        ('WNA', 'WNA'),
    )
    JENIS_KELAMIN = (
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    )
    AGAMA_SISWA_CHOICES = (
        ('','Pilih agama'),
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
        ('Kong Hu Cu', 'Kong Hu Cu'),
    )
    STATUS_TINGGAL_SISWA = (
        ('', 'Pilih status tinggal'),
        ('Tinggal dengan ORTU/WALI', 'Tinggal dengan ORTU/WALI'),
        ('Ikut Saudara/Kerabat', 'Ikut Saudara/Kerabat'),
        ('Asrama', 'Asrama'),
        ('Kontrak/Kost', 'Kontrak/Kost'),
        ('Panti Asuhan', 'Panti Asuhan'),
        ('lainnya', 'Lainnya'),
    )
    TRANSPOSTASI_SISWA = (
        ('', 'Pilih transportasi'),
        ('Jalan Kaki', 'Jalan Kaki'),
        ('Sepeda', 'Sepeda'),
        ('Sepeda Motor', 'Sepeda Motor'),
        ('Mobil Pribadi', 'Mobil Pribadi'),
        ('Angkutan Umum', 'Angkutan Umum'),
        ('lainnya', 'Lainnya'),
    )
    JARAK_TEMPUH = (
        ('', 'Pilih jarak tempuh'),
        ('<5km', 'Kurang dari 5KM'),
        ('5-10km', 'Antara 5-10M'),
        ('11-20km', 'Antara 11-20KM'),
        ('21-30km', 'Antara 21-30KM'),
        ('>30km', 'Lebih dari 30KM'),
    )
    WAKTU_TEMPUH = (
        ('', 'Waktu tempuh'),
        ('1-10m', '1-10 menit'),
        ('10-19m', '10-19 menit'),
        ('20-29m', '20-29 menit'),
        ('30-39m', '30-39 menit'),
        ('1-2j', '1-2 jam'),
        ('>2j', 'Lebih dari 2 jam'),
    )
    BIAYA_SEKOLAH = (
        ('', 'Biaya sekolah'),
        ('Orangtua', 'Orangtua'),
        ('Wali/Orangtua Asuh', 'Wali/Orangtua Asuh'),
        ('Tanggung Sendiri', 'Tanggung Sendiri'),
        ('Lainnya', 'Lainnya'),
    )
    KEBUTUHAN_KHUSUS = (
        ('', 'Kebutuhan khusus'),
        ('Tidak Ada', 'Tidak Ada'),
        ('Lamban Belajar', 'Lamban Belajar'),
        ('Kesulitan Belajar Spesifik', 'Kesulitan Belajar Spesifik'),
        ('Gangguan Komunikasi', 'Gangguan Komunikasi'),
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
    PRA_SEKOLAH = (
        ('', 'Pra sekolah'),
        ('Tidak Keduanya', 'Tidak Keduanya'),
        ('Pernah TK/RA', 'Pernah TK/RA'),
        ('Pernah PAUD', 'Pernah PAUD'),
    )
    GOL_DARAH = (
        ('', 'Golongan darah'),
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
    )
    KETERANGAN = (
        ('Pending', 'Pending'),
        ('Diterima', 'Diterima'),
        ('Ditolak', 'Ditolak'),
    )
    KIP = (
        ('Ya', 'Ya'),
        ('No', 'Tidak'),
    )
    PKH_KKS = (
        ('Ya', 'Ya'),
        ('No', 'Tidak'),
    )
    thn_ajaran              = models.ForeignKey(Pengaturan_PPDB, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tahun Ajaran")
    nisn                    = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="NISN")
    no_pendaftaran          = models.CharField('No Pendaftaran', max_length=15, unique=True, null=True, blank=True, editable=True)
    nama                    = models.CharField('Nama Lengkap', max_length=60)
    asal_sekolah            = models.CharField('Asal Sekolah', max_length=60)
    status                  = models.CharField('Status', max_length=10, choices=STATUS_PESERTA_CHOICES, default=1)
    warga_siswa             = models.CharField('Warna Negara', max_length=3, choices=STATUS_WARGA_NEGARA, default=1)
    jenis_kelamin           = models.CharField('Jenis Kelamin', max_length=15, choices=JENIS_KELAMIN, default="")
    nik                     = models.CharField('NIK', max_length=16)
    tempat_lahir            = models.CharField('Tempat Lahir', max_length=30)
    tgl_lahir               = models.DateField('Tanggal Lahir')
    anak_ke                 = models.CharField('Anak Ke', max_length=2, null=True, blank=True)
    saudara                 = models.CharField('Jumlah Saudara', max_length=2, null=True, blank=True)
    agama                   = models.CharField('Agama', max_length=10, choices=AGAMA_SISWA_CHOICES)
    cita                    = models.CharField('Cita-cita', max_length=20, null=True, blank=True)
    no_hp                   = models.CharField('No Telp/Wa', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    email                   = models.CharField('Email', max_length=35, null=True, blank=True)
    hobi                    = models.CharField('Hobi', max_length=15, null=True, blank=True)
    status_tinggal_siswa    = models.CharField('Status Tinggal', max_length=50, choices=STATUS_TINGGAL_SISWA)
    alamat_siswa            = models.TextField('Alamat')
    kodepos_siswa           = models.CharField('Kode POS', max_length=6, null=True, blank=True)
    transportasi            = models.CharField('Transportasi', max_length=30, choices=TRANSPOSTASI_SISWA, null=True, blank=True)
    jarak                   = models.CharField('Jarak Tempuh', max_length=20, choices=JARAK_TEMPUH, null=True, blank=True)
    waktu                   = models.CharField('Waktu Tempuh', max_length=20, choices=WAKTU_TEMPUH, null=True, blank=True)
    biaya_sekolah           = models.CharField('Biaya Sekolah', max_length=30, choices=BIAYA_SEKOLAH)
    keb_khusus              = models.CharField('Kebutuhan Khusus', max_length=30, choices=KEBUTUHAN_KHUSUS)
    keb_disabilitas         = models.CharField('Kebutuhan Disabilitas', max_length=20, choices=KEBUTUHAN_DISABILITAS)
    pra_sekolah             = models.CharField('Pra Sekolah', max_length=20, choices=PRA_SEKOLAH, null=True, blank=True)
    gol_darah               = models.CharField('Golongan Darah', max_length=2, choices=GOL_DARAH, null=True, blank=True)
    kip                     = models.CharField('KIP', max_length=5, choices=KIP, default="", help_text='Jika ada.')
    no_kip                  = models.CharField('No KIP', max_length=20, null=True, blank=True, help_text='Isi jika ada.')
    pkh_kks                 = models.CharField('PKH/KKS', max_length=5, choices=PKH_KKS, default="", help_text='Jika ada.')
    no_pkh_kks              = models.CharField('No PKH/KKS', max_length=20, null=True, blank=True, help_text='Isi jika ada.')
    foto_peserta_didik      = models.ImageField('Foto Peserta', max_length=255, upload_to=image_upload_to, help_text='foto 3x4 dengan background merah')
    Keterangan              = models.CharField('Keterangan', max_length=10, null=True, choices=KETERANGAN, default="Pending")
    tgl_daftar              = models.DateTimeField('Tanggal Daftar', auto_now_add=True, null=True, blank=True, editable=False)

    # data tuple ortu
    STATUS_ORTU = (
        ('', 'Status'),
        ('Masih Hidup', 'Masih Hidup'),
        ('Sudah Meninggal', 'Sudah Meninggal'),
        ('Tidak Diketahui', 'Tidak Diketahui'),
    )
    STATUS_WALI = (
        ('', 'Status Wali'),
        ('Sama dengan Ayah', 'Sama dengan Ayah'),
        ('Sama dengan Ibu', 'Sama dengan Ibu'),
        ('Lainnya', 'Lainnya'),
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
    DOMISILI_ORTU = (
        ('', 'Domisili'),
        ('Dalam Negri', 'Dalam Negri'),
        ('Luar Negri', 'Luar Negri'),
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
    # ayah
    nama_ayah               = models.CharField('Nama Lengkap Ayah', max_length=30, null=True, blank=True)
    status_ayah             = models.CharField('Status Ayah', max_length=30, choices=STATUS_ORTU, null=True, blank=True)
    warga_ayah              = models.CharField('Warga Negara Ayah', max_length=20, choices=STATUS_WARGA_NEGARA, null=True, blank=True)
    nik_ayah                = models.CharField('NIK Ayah', max_length=30, null=True, blank=True)
    tempat_lahir_ayah       = models.CharField('Tempat Lahir Ayah', max_length=20, null=True, blank=True)
    tgl_lahir_ayah          = models.DateField('Tanggal Lahir Ayah', null=True, blank=True)
    pendidikan_ayah         = models.CharField('Pendidikan Ayah', max_length=25, choices=PENDIDIKAN_ORTU, null=True, blank=True)
    pekerjaan_ayah          = models.CharField('Pekerjaan Ayah', max_length=50, choices=PEKERJAAN_ORTU, null=True, blank=True)
    penghasilan_ayah        = models.CharField('Penghasilan Ayah', max_length=30, choices=PENGHASILAN_ORTU, null=True, blank=True)
    no_hp_ayah              = models.CharField('No Telp/Wa', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    domisili_ayah           = models.CharField('Domisili Ayah', max_length=25, choices=DOMISILI_ORTU, null=True, blank=True)
    status_tmp_tinggal_ayah = models.CharField('Status Tempat Tinggal Ayah', max_length=25, choices=STATUS_TINGGAL_ORTU, null=True, blank=True)
    alamat_ayah             = models.TextField('Alamat Ayah', null=True, blank=True)
    kodepos_ayah            = models.CharField('Kode POS', max_length=8, null=True, blank=True)
    # ibu
    nama_ibu                = models.CharField('Nama Lengkap Ibu', max_length=30, null=True, blank=True)
    status_ibu              = models.CharField('Status Ibu', max_length=30, choices=STATUS_ORTU, null=True, blank=True)
    warga_ibu               = models.CharField('Warna Negara Ibu', max_length=20, choices=STATUS_WARGA_NEGARA, null=True, blank=True)
    nik_ibu                 = models.CharField('NIK Ibu', max_length=30,  null=True, blank=True)
    tempat_lahir_ibu        = models.CharField('Tempat Lahir Ibu', max_length=20, null=True, blank=True)
    tgl_lahir_ibu           = models.DateField('Tanggal Lahir Ibu', null=True, blank=True)
    pendidikan_ibu          = models.CharField('Pendidikan Ibu', max_length=25, choices=PENDIDIKAN_ORTU, null=True, blank=True)
    pekerjaan_ibu           = models.CharField('Pekerjaan Ibu', max_length=30, choices=PEKERJAAN_ORTU, null=True, blank=True)
    penghasilan_ibu         = models.CharField('Penghasilan Ibu', max_length=25, choices=PENGHASILAN_ORTU, null=True, blank=True)
    no_hp_ibu               = models.CharField('No Telp/Wa', max_length=13, null=True, blank=True, help_text='Pastikan nomer aktif dan dapat dihubungi.')
    domisili_ibu            = models.CharField('Domisili Ibu', max_length=25, choices=DOMISILI_ORTU, null=True, blank=True)
    alamat_ibu              = models.TextField('Alamat Ibu', null=True, blank=True)
    kodepos_ibu             = models.CharField('Kode POS', max_length=8, null=True, blank=True)
    # wali
    nama_wali               = models.CharField('Nama Wali', max_length=30, null=True, blank=True)
    status_wali             = models.CharField('Status Wali', max_length=25, choices=STATUS_WALI, default="")
    warga_wali              = models.CharField('Warga Negara Wali', max_length=25, choices=STATUS_WARGA_NEGARA, null=True, blank=True)
    nik_wali                = models.CharField('NIK Wali', max_length=30, null=True, blank=True)
    tempat_lahir_wali       = models.CharField('Tempat Lahir Wali', max_length=30, null=True, blank=True)
    tgl_lahir_wali          = models.DateField('Tanggal Lahir Wali', null=True, blank=True)
    pendidikan_wali         = models.CharField('Pendidikan Wali', max_length=25, choices=PENDIDIKAN_ORTU, null=True, blank=True)
    pekerjaan_wali          = models.CharField('Pekerjaan Wali', max_length=30, choices=PEKERJAAN_ORTU, null=True, blank=True)
    penghasilan_wali        = models.CharField('Penghasilan Wali', max_length=25, choices=PENGHASILAN_ORTU, null=True, blank=True)
    no_hp_wali              = models.CharField('No Telp/Wa Wali', max_length=15, null=True, blank=True)
    domisili_wali           = models.CharField('Domisili Wali', max_length=25, choices=DOMISILI_ORTU, null=True, blank=True)
    alamat_wali             = models.TextField('Alamat Wali', null=True, blank=True)
    kodepos_wali            = models.CharField('Kode POS', max_length=8, null=True, blank=True)
    # dokumen pendukung
    file_kip                = models.FileField('Kartu Indonesia Pintar', max_length=255, upload_to=file_upload_to, help_text='(Jika ada). Mendukung format file dan gambar.', null=True, blank=True)
    file_pkh                = models.FileField('Kartu PKH/KKS', max_length=255, upload_to=file_upload_to, help_text='(Jika ada). Mendukung format file dan gambar.', null=True, blank=True)
    file_kk                 = models.FileField('Kartu Keluarga', max_length=255, upload_to=file_upload_to, help_text='Mendukung format file dan gambar.')
    file_akte               = models.FileField('Akta Kelahiran', max_length=255, upload_to=file_upload_to, help_text='Mendukung format file dan gambar.')
    file_raport             = models.FileField('Nilai Raport Terakhir', max_length=255, upload_to=file_upload_to, help_text='Mendukung format file dan gambar.')
    file_skl                = models.FileField('Surat Keterangan Lulus', max_length=255, upload_to=file_upload_to, help_text='Mendukung format file dan gambar.')
    file_ijazah             = models.FileField('Ijazah Jenjang Sebelumnya', max_length=255, upload_to=file_upload_to, help_text='(Jika sudah ada). Mendukung format file dan gambar.', null=True, blank=True)
    file_skhun              = models.FileField('SKHUN', max_length=255, upload_to=file_upload_to, help_text='(Jika sudah ada). Mendukung format file dan gambar.', null=True, blank=True)
    konfirmasi              = models.BooleanField('Ya, data sudah sesuai dan lengkap.')
            
    # preview image/file
    def foto_peserta(self):
        try:
            return mark_safe(f'<img src = "{self.foto_peserta_didik.url}" width = "75"/>')
        except:
            pass
    
    def kip_preview(self):
        return mark_safe(f'<img src = "{self.file_kip.url}" width = "275"/>')
    
    def pkh_preview(self):
        return mark_safe(f'<img src = "{self.file_pkh.url}" width = "275"/>')
    
    def kk_preview(self):
        return mark_safe(f'<img src = "{self.file_kk.url}" width = "275"/>')
    
    def akte_preview(self):
        return mark_safe(f'<img src = "{self.file_akte.url}" width = "275"/>')
    
    def raport_preview(self):
        return mark_safe(f'<img src = "{self.file_raport.url}" width = "275"/>')
    
    def skl_preview(self):
        return mark_safe(f'<img src = "{self.file_skl.url}" width = "275"/>')
    
    def ijazah_preview(self):
        return mark_safe(f'<img src = "{self.file_ijazah.url}" width = "275"/>')
    
    def skhun_preview(self):
        return mark_safe(f'<img src = "{self.file_skhun.url}" width = "275"/>')

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

    class Meta:
        verbose_name = "Peserta PPDB"
        verbose_name_plural = "Peserta PPDB"


class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("user", self.username, instance)
        return None

    description = models.TextField('Deskripsi Profil', max_length=600, default="", blank=True)
    image       = models.ImageField('Foto Profil', default='default/user.png', upload_to=image_upload_to)    

    def __str__(self):
        return self.username