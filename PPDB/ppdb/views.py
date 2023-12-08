from django.shortcuts import render, redirect
from . forms import UserRegistraionForm, PesertaForm, UpdatePesertaForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control #destroy the section after logout
from . models import Pengaturan_PPDB, Peserta

# Create your views here.
# ============== BACKEND ==============|
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def datamaster(request, pk):
    try:
        data = Peserta.objects.filter(nisn=request.user).get(nisn=pk)
    except Peserta.DoesNotExist:
        data = None
        messages.info(request, f"Tidak ada data yang cocok, silahkan isi data terlebih dahulu di <b>Form Pendaftaran</b>")
        return redirect('ppdb:form')
    
    if request.method == "POST":
        form = UpdatePesertaForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UpdatePesertaForm(instance=data)
        context = {
            'form': form,
        }
    return render(request, 'ppdb/form.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def formulir(request):
    nisn = request.user 
    thn = Pengaturan_PPDB.objects.filter(status="Dibuka").last()

    if request.method == "POST":
        form = PesertaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulir berhasil diajukan, silahkan tunggu verifikasi data")
            return redirect('ppdb:form')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:form')
    
    form = PesertaForm(initial={'nisn':nisn, 'thn_ajaran':thn})
    context = {
        'page_title': 'Formulir PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
    }
    return render(request, 'ppdb/form.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    '''fungsi menampilkan dashboard'''

    context = {
        'page_title': 'Dashboard PPDB | SMP Miftahul Falah Gandrungmangu',
    }
    return render(request, 'ppdb/dashboard.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_user(request):
    '''fungsi logout'''

    logout(request)
    messages.success(request, "Anda berhasil keluar dari halaman dashbaord")
    return redirect('ppdb:index')



# ============== FRONTEND ==============|
def login_user(request):
    '''fungsi login user'''

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
        'page_title': 'Login Siswa | SMP Miftahul Falah Gandrungmangu',
        'sub_title': 'PPDB Online | SMP Miftahul Falah Gandrungmangu',
        'heading': 'Halaman Login Siswa',
    }
    return render(request, 'auth.html', context)

def register(request):
    '''fungsi untuk registrasi akun ppdb peserta'''

    if request.method == "POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"akun berhasil di tambahkan {user.username}") 
            return redirect('ppdb:login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)


    form = UserRegistraionForm()
    context ={
        'form': form,
        'page_title': 'Daftar Akun PPDB | SMP Miftahul Falah Gandrungmangu',
        'sub_title': 'PPDB Online | SMP Miftahul Falah Gandrungmangu',
        'heading': 'Form Pendaftaran Akun'
    }
    return render(request, 'auth.html', context)

def index(request):
    '''ini adalah fungsi menampilkan halaman index'''

    peserta = Peserta.objects.all().order_by('-tgl_daftar')
    info_ppdb = Pengaturan_PPDB.objects.all().order_by('-pk').first()

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