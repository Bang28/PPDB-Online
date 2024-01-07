from django.shortcuts import render, redirect
from ppdb.models import Siswa, TahunAjaran
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime
from django.contrib import messages


# ============== BACKEND ==============|
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    '''fungsi menampilkan template dashboard'''

    total = Siswa.objects.all().count()
    terima = Siswa.objects.filter(verifikasi="Diterima").count()
    pending = Siswa.objects.filter(verifikasi="Pending").count()
    date = datetime.now().date()
    hari = Siswa.objects.filter(tgl_daftar__gt = date)


    context = {
        'page_title': 'Dashboard PPDB | SMP Miftahul Falah Gandrungmangu',
        'total': total,
        'terima': terima,
        'pending': pending,
        'today': hari,
    }
    return render(request, 'ppdb/dashboard.html', context)


# ============== FRONTEND ==============|
def index(request):
    '''fungsi menampilkan halaman index'''

    peserta = Siswa.objects.all().order_by('-tgl_daftar')
    info_ppdb = TahunAjaran.objects.all().order_by('-pk').first()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hello {user.first_name} {user.last_name}, selamat datang didashboard PPDB")
            return redirect('ppdb:dashboard')
        else:
            messages.error(request, 'Login gagal, silahkan periksa username & password anda')

    context = {
        'page_title': 'PPDB Online | SMP Miftahul Falah Gandrungmangu',
        'ppdb': info_ppdb,
        'peserta': peserta,
    }
    return render(request, 'index.html', context)