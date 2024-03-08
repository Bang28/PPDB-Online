from ppdb.models import Siswa, OrangTua, Wali, Berkas, TahunAjaran
from django.db import connection

def run():

    obj_siswa = Siswa.objects.all().filter('nama')
    # obj_ortu = obj_siswa.ortu
    # print(connection.queries)



    print(obj_siswa)
    # print(obj_ortu)
    # print(obj_siswa.berkas)
    # print(connection.queries)
