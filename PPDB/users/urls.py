from django.urls import path

from . views import (
    register,
    loginUser,
    loginAdmin,
    logoutUser,
    pengguna,
    userProfile,
    hapusPengguna,
    tambahPengguna,
    editPengguna,
)

app_name = "users"
urlpatterns = [
    # ====== PATH TO FRONTEND ======|
    path('register/', register, name="register"),
    path('login_user/', loginUser, name="login"),
    path('login_admin/', loginAdmin, name="admin"),


    # ====== PATH TO BACKEND ======|
    path('logout/', logoutUser, name="logout"),
    path('', pengguna, name="pengguna"),
    path('profile/<username>', userProfile, name="profile"),
    path('tambah_pengguna/', tambahPengguna, name="tambah-pengguna"),
    path('edit_pengguna/', editPengguna, name="edit-pengguna"),
    path('hapus_pengguna/<pengguna_id>', hapusPengguna, name="hapus-pengguna"),
]