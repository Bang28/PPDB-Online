from ppdb.models import Siswa, OrangTua, Wali, Berkas, TahunAjaran
from django.db import connection

def run():

    obj_siswa = Siswa.objects.filter(id_siswa=2).first()
    obj_ortu = obj_siswa.ortu
    # print(connection.queries)



    print(obj_siswa)
    print(obj_ortu)
    # print(obj_siswa.berkas)
    # print(connection.queries)


# class Siswa(models.Model):
#     id_siswa   = models.BigAutoField(primary_key=True, unique=True, auto_created=True)
#     nama       = models.CharField('Nama Lengkap', max_length=55)

# class OrangTua(models.Model):
#     id_ortu    = models.BigAutoField(primary_key=True, unique=True, auto_created=True)
#     nama       = models.CharField('Nama Lengkap', max_length=30, null=True, blank=True)
#     siswa      = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='ortu')

# class Wali(models.Model):
#     id_wali    = models.BigAutoField(primary_key=True, unique=True, auto_created=True)
#     nama       = models.CharField('Nama Wali', max_length=30, null=True, blank=True)
#     siswa      = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='wali')

# class Berkas(models.Model):
#     id_berkas  = models.BigAutoField(primary_key=True, unique=True, auto_created=True)
#     file_skl   = models.FileField('Surat Keterangan Lulus', max_length=255, upload_to=file_skl, validators=[file_extension, file_size])
#     siswa      = models.OneToOneField(Siswa, on_delete=models.CASCADE, related_name='berkas')
