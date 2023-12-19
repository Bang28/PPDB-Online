from django.urls import path

from . views import (
    register,
    loginUser,
    logoutUser,
    pengguna,
    hapusPengguna,
    tambahPengguna,
    editPengguna,
)

app_name = "users"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('register/', register, name="register"),
    path('login/', loginUser, name="login"),


    # ====== PATH TO BACKEND ======|
    path('logout/', logoutUser, name="logout"),
    path('', pengguna, name="pengguna"),
    path('tambah_pengguna/', tambahPengguna, name="tambah-pengguna"),
    path('edit_pengguna/<pengguna_id>', editPengguna, name="edit-pengguna"),
    path('hapus_pengguna/<pengguna_id>', hapusPengguna, name="hapus-pengguna"),
]