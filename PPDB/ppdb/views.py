from django.shortcuts import render, redirect
from . forms import UserRegistraionForm, PesertaForm, UpdatePesertaForm, EmailForm, PengaturanPPDBForm, PenggunaForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control #destroy the section after logout
from . decorators import user_is_superuser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from . models import PeriodePPDB, Peserta
from datetime import datetime
from django.core.mail import EmailMessage

# Create your views here.
# ============== BACKEND ==============|
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def email(request):
    '''fungsi mengirimkan email ke peserta menggunakan SMTP Mail'''

    if request.method == "POST":
        form = EmailForm(request.POST, request.FILES)

        instansi = "SMP Miftahul Falah Gandrungmangu"

        if form.is_valid():

            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            cc = form.cleaned_data["cc"]
            file = request.FILES.getlist('attach')

            mail = EmailMessage(subject, message, instansi, [email], [cc])
            for f in file:
                mail.attach(f.name, f.read(), f.content_type)
            mail.send()

            messages.success(request, "Email behasil dikirim")
            return redirect('ppdb:data-diterima')
    else:
        form = EmailForm()
        return render(request, {'form': form})

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusPengguna(request, pengguna_id):
    '''fungsi hapus data pengguna'''

    pengguna = User.objects.get(id=pengguna_id)
    pengguna.delete()
    messages.success(request, "Data pengguna berhasil dihapus!")
    return redirect('ppdb:pengguna')

@login_required(login_url="ppdb:login")
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
            return redirect("ppdb:pengguna")
        
@login_required(login_url="ppdb:login")
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
            return redirect('ppdb:pengguna')
    else:
        return render(request, 'ppdb/modals/tambahPengguna.html')

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def pengguna(request):
    '''fungsi menampilkan semua data pengguna'''

    user = User.objects.all().order_by('date_joined')
    return render(request, 'ppdb/users/pengguna.html', {'users': user})

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userProfile(request):
    pass

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusData(request, id):
    '''fungsi hapus data peserta ppdb'''

    peserta = Peserta.objects.get(id=id)
    peserta.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:data-pendaftar")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tolakForm(request):
    '''fungsi menginput nilai dari template viewData'''

    if request.method == "POST":
        peserta = Peserta.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.Keterangan = request.POST.get('Keterangan')
            peserta.save()
            messages.success(request, "Formulir ditolak, silahkan kirim balasan ke peserta")
            return redirect("ppdb:view-data")
        
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def terimaForm(request):
    '''fungsi menginput nilai dari template viewData'''

    if request.method == "POST":
        peserta = Peserta.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.Keterangan = request.POST.get('Keterangan')
            peserta.save()
            messages.success(request, "Formulir diterima, silahkan kirim balasan ke peserta")
            return redirect("ppdb:data-diterima")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def viewData(request, id):
    '''fungsi menampilkan detail data peserta'''

    peserta = Peserta.objects.get(id=id)
    if peserta != None:
        return render(request, 'ppdb/viewData.html', {'peserta': peserta})


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataDiterima(request):
    '''fungsi menampilkan data peserta berdasarkan data peserta diterima'''

    peserta = Peserta.objects.filter(Keterangan="Diterima")
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataDiterima.html', context)


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataPendaftar(request):
    '''fungsi menampilkan semua data pendaftar'''

    peserta = Peserta.objects.all().order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataPendaftar.html', context)


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataMaster(request, pk):
    '''fungsi view data dan edit data master peserta berdasarkan request user'''

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
    '''fungsi menampilkan template formulir pendaftaran'''

    nisn = request.user 
    thn = PeriodePPDB.objects.filter(status="Dibuka").last()

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
@user_is_superuser
def hapusDataPPDB(request, periode_id):
    '''fungsi hapus data periode ppdb'''

    pengaturan = PeriodePPDB.objects.get(id=periode_id)
    pengaturan.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:pengaturan-ppdb")


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def editPeriode(request, periode_id):
    '''fungsi untuk merubah data periode ppdb'''

    if request.method == "POST":
        periode = PeriodePPDB.objects.get(id = periode_id)
        if periode != None:
            periode.tahun_ajaran = request.POST.get('tahun_ajaran')
            periode.tanggal_mulai = request.POST.get('tanggal_mulai')
            periode.tanggal_selesai = request.POST.get('tanggal_selesai')
            periode.status = request.POST.get('status')
            periode.save()
            messages.success(request, "Data Periode berhasil diperbarui!")   
            return redirect("ppdb:pengaturan-ppdb")
    
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tambahPeriode(request):
    '''fungsi menambahkan data periode ppdb'''

    if request.method == "POST":
        if request.POST.get('tahun_ajaran') \
            and request.POST.get('tanggal_mulai') \
            and request.POST.get('tanggal_selesai') \
            or request.POST.get('status'):
            periode = PeriodePPDB()
            periode.tahun_ajaran = request.POST.get('tahun_ajaran')
            periode.tanggal_mulai = request.POST.get('tanggal_mulai')
            periode.tanggal_selesai = request.POST.get('tanggal_selesai')
            periode.status = request.POST.get('status')
            periode.save()
            messages.success(request, "Data Periode berhasil ditambahkan!")
            return redirect("ppdb:pengaturan-ppdb")
    else:
        return render(request, 'ppdb/modals/tambahPeriode.html')

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def pengaturanPPDB(request):
    '''fungsi untuk menampilkan semua data periode ppdb'''

    pengaturan = PeriodePPDB.objects.all().order_by('-pk')

    if request.method == "POST":
        form = PengaturanPPDBForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "PPDB periode berhasil ditambahkan.")
            return redirect("ppdb:pengaturan-ppdb")

    form = PengaturanPPDBForm()
    context = {
        'pengaturan': pengaturan,
        'heading': 'Tambah Periode PPDB',
        'button': 'Tambah',
        'form': form
    }
    return render(request, 'ppdb/pengaturanPpdb.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    '''fungsi menampilkan template dashboard'''

    total = Peserta.objects.all().count()
    terima = Peserta.objects.filter(Keterangan="Diterima").count()
    pending = Peserta.objects.filter(Keterangan="Pending").count()
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

@login_required(login_url="ppdb:login")
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
    return render(request, 'auth.html', context)

def register(request):
    '''fungsi untuk registrasi akun ppdb peserta'''

    ppdb_info = PeriodePPDB.objects.all().order_by('-pk').first()

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
    '''fungsi menampilkan halaman index'''

    peserta = Peserta.objects.all().order_by('-tgl_daftar')
    info_ppdb = PeriodePPDB.objects.all().order_by('-pk').first()

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


# ============== ERRORS HANDLER ==============|
def error_404(request, exception):
    '''fungsi menampilkan template error 404'''
    return render(request, 'ppdb/404.html')

def error_505(request, exception):
    '''fungsi menampilkan template error 505'''
    return render(request, 'ppdb/505.html')