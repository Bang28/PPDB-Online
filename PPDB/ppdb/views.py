from django.shortcuts import render, redirect
from . forms import UserRegistraionForm, PesertaForm, UpdatePesertaForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control #destroy the section after logout
from . decorators import user_is_superuser
from django.contrib.auth.models import User
from . models import Pengaturan_PPDB, Peserta
from datetime import datetime

# Create your views here.
# ============== BACKEND ==============|
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def userList(request):
    user = User.objects.all().order_by('date_joined')
    return render(request, 'ppdb/users/userList.html', {'users': user})

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userProfile(request):
    pass

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def userAdd(request):
    pass

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusdata(request, id):
    peserta = Peserta.objects.get(id=id)
    peserta.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:dpendaftar")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tolak(request):
    if request.method == "POST":
        peserta = Peserta.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.Keterangan = request.POST.get('Keterangan')
            peserta.save()
            messages.success(request, "Formulir ditolak, silahkan kirim balasan ke peserta")
            return redirect("pppdb:viewdata")
        
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def markdata(request):
    if request.method == "POST":
        peserta = Peserta.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.Keterangan = request.POST.get('Keterangan')
            peserta.save()
            messages.success(request, "Formulir diterima, silahkan kirim balasan ke peserta")
            return redirect("pppdb:viewdata")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def viewdata(request, id):
    peserta = Peserta.objects.get(id=id)
    if peserta != None:
        return render(request, 'ppdb/viewdata.html', {'peserta': peserta})


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataditerima(request):
    peserta = Peserta.objects.filter(Keterangan="Diterima")
    print(peserta)
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataDiterima.html', context)


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def datapendaftar(request):
    peserta = Peserta.objects.all().order_by('-tgl_daftar')
    print(peserta)
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataPendaftar.html', context)


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

    total = Peserta.objects.all().count()
    terima = Peserta.objects.filter(Keterangan="Diterima").count()
    pending = Peserta.objects.filter(Keterangan="Pending").count()
    date = datetime.now().date()
    hari = Peserta.objects.filter(tgl_daftar__gt = date).count()


    context = {
        'page_title': 'Dashboard PPDB | SMP Miftahul Falah Gandrungmangu',
        'total': total,
        'terima': terima,
        'pending': pending,
        'today': hari,
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

    ppdb_info = Pengaturan_PPDB.objects.all().order_by('-pk').first()

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
        'heading': 'Form Pendaftaran Akun',
        'ppdb': ppdb_info,
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