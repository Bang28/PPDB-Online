from django.shortcuts import render, redirect
from ppdb.models import Peserta, TahunAjaran
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime
from django.contrib import messages


# ============== BACKEND ==============|
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    '''fungsi menampilkan template dashboard'''

    total = Peserta.objects.all().count()
    terima = Peserta.objects.filter(verifikasi="Diterima").count()
    pending = Peserta.objects.filter(verifikasi="Pending").count()
    date = datetime.now().date()
    hari = Peserta.objects.filter(tgl_daftar__gt = date)


    context = {
        'page_title': 'Dashboard PPDB | SMP Miftahul Falah Gandrungmangu',
        'total': total,
        'terima': terima,
        'pending': pending,
        'today': hari,
    }
    return render(request, 'ppdb/dashboard.html', context)


# ============== FRONTEND ==============|
def pendaftar(request):
    '''fungsi menampilkan data pendaftar'''
    
    info_ppdb = TahunAjaran.objects.last()
    peserta = Peserta.objects.all().order_by('-tgl_daftar')

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
        'peserta': peserta,
        'ppdb': info_ppdb,
    }
    return render(request, 'pendaftar.html', context)

def index(request):
    '''fungsi menampilkan halaman index'''
    
    info_ppdb = TahunAjaran.objects.last()
    print(info_ppdb)

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
    }
    return render(request, 'index.html', context)