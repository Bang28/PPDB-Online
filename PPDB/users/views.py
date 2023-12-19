from django.shortcuts import render, redirect
from ppdb.models import PeriodePPDB, Peserta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from . forms import UserRegistraionForm, PenggunaForm
from . decorators import user_is_superuser
from django.contrib.auth.models import User

# Create your views here.
# ============== BACKEND ==============|
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userProfile(request):
    pass

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusPengguna(request, pengguna_id):
    '''fungsi hapus data pengguna'''

    pengguna = User.objects.get(id=pengguna_id)
    pengguna.delete()
    messages.success(request, "Data pengguna berhasil dihapus!")
    return redirect('users:pengguna')

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def editPengguna(request, pengguna_id):
    '''fungsi edit data pengguna'''

    if request.method == "POST":
        pengguna = User.objects.get(id = pengguna_id)
        if pengguna != None:
            pengguna.username = request.POST.get('username')
            pengguna.first_name = request.POST.get('first_name')
            pengguna.last_name = request.POST.get('last_name')
            pengguna.email = request.POST.get('email')
            pengguna.is_active = request.POST.get('is_active')
            pengguna.is_staff = request.POST.get('is_staff')
            pengguna.is_superuser = request.POST.get('is_superuser')
            pengguna.save()
            messages.success(request, "Data pengguna berhasil diperbarui")
            return redirect("users:pengguna")

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tambahPengguna(request):
    '''fungsi menambahkan data pengguna'''

    if request.method == "POST":
        if request.POST.get('username') \
            and request.POST.get('first_name') \
            and request.POST.get('last_name') \
            and request.POST.get('email') \
            and request.POST.get('is_active') \
            and request.POST.get('is_superuser') \
            or request.POST.get('password'):
            pengguna = PenggunaForm(request.POST or None)
            pengguna.username = request.POST.get('username') 
            pengguna.first_name = request.POST.get('first_name') 
            pengguna.last_name = request.POST.get('last_name') 
            pengguna.email = request.POST.get('email') 
            pengguna.is_active = request.POST.get('is_active') 
            pengguna.is_superuser = request.POST.get('is_superuser') 
            pengguna.password = request.POST.get('password')
            pengguna.save()
            messages.success(request, "Pengguna baru berhasil ditambahan!")
            return redirect('users:pengguna')
    else:
        return render(request, 'users/modals/tambahPengguna.html')

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def pengguna(request):
    '''fungsi menampilkan semua data pengguna'''

    user = User.objects.all().order_by('date_joined')
    return render(request, 'users/pengguna.html', {'users': user})

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logoutUser(request):
    '''fungsi logout user'''

    logout(request)
    messages.success(request, "Anda berhasil keluar dari halaman dashbaord")
    return redirect('ppdb:index')



# ============== FRONTEND ==============|
def loginUser(request):
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
    return render(request, 'users/auth.html', context)

def register(request):
    '''fungsi untuk registrasi akun ppdb peserta'''

    ppdb_info = PeriodePPDB.objects.all().order_by('-pk').first()

    if request.method == "POST":
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"akun berhasil di tambahkan {user.username}") 
            return redirect('users:login')
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
    return render(request, 'users/auth.html', context)