from django.shortcuts import render, redirect
from . forms import FormulirForm, UpdateFormulirForm, EmailForm, TahunAjaranForm, DataAyahForm, DataIbuForm, DataWaliForm, BerkasForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.decorators.cache import cache_control #destroy the section after logout
from . decorators import user_is_superuser
from . models import TahunAjaran, Formulir
from datetime import datetime
from django.core.mail import EmailMessage


# Create your views here.
def singleForm(request):
    '''fungsi menampilkan template formulir datadiri'''

    nisn = request.user 
    thn = TahunAjaran.objects.filter(status="Dibuka").last()

    if request.method == "POST":
        form = FormulirForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Datadiri disimpan, silahkan lengkapi data berikut!")
            return redirect('ppdb:form')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:multi')
    
    form = FormulirForm(initial={'nisn':nisn, 'thn_ajaran':thn})
    context = {
        'page_title': 'Formulir PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
    }
    return render(request, 'ppdb/formulir.html', context)

def multiForm(request):
    '''fungsi untuk menampilkan formulir Data & Berkas'''
    id_form = Formulir.objects.last()
    
    forms = [
        DataAyahForm(request.POST or None),
        DataWaliForm(request.POST or None),
        DataIbuForm(request.POST or None),
        BerkasForm(request.POST, request.FILES or None),
    ]

    if request.method == "POST":
        if all(forms[i].is_valid() for i in range(len(forms))):
            for form in forms:
                form.save()
            messages.success(request, 'berhasil')
            return redirect('ppdb:dashboard')
    
    forms = [
        DataAyahForm(initial={'peserta': id_form}),
        DataWaliForm(initial={'peserta': id_form}),
        DataIbuForm(initial={'peserta': id_form}),
        BerkasForm(initial={'peserta': id_form}),
    ]
    context = {
        'page_title': 'Formulir PPDB | SMP Miftahul Falah Gandrungmangu',
        'forms': forms,
    }
    return render(request, 'ppdb/multiform.html', context)


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
def hapusData(request, id):
    '''fungsi hapus data peserta ppdb'''

    peserta = Formulir.objects.get(id=id)
    peserta.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:data-pendaftar")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tolakForm(request):
    '''fungsi menginput nilai dari template viewData'''

    if request.method == "POST":
        peserta = Formulir.objects.get(id = request.POST.get('id'))
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
        peserta = Formulir.objects.get(id = request.POST.get('id'))
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

    peserta = Formulir.objects.get(id=id)
    if peserta != None:
        return render(request, 'ppdb/viewData.html', {'peserta': peserta})


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataDiterima(request):
    '''fungsi menampilkan data peserta berdasarkan data peserta diterima'''

    peserta = Formulir.objects.filter(Keterangan="Diterima")
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataDiterima.html', context)


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataPendaftar(request):
    '''fungsi menampilkan semua data pendaftar'''

    peserta = Formulir.objects.all().order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataPendaftar.html', context)


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataMaster(request, pk):
    '''fungsi view data dan edit data master peserta berdasarkan request user'''

    try:
        data = Formulir.objects.filter(nisn=request.user).get(nisn=pk)
    except Formulir.DoesNotExist:
        data = None
        messages.info(request, f"Tidak ada data yang cocok, silahkan isi data terlebih dahulu di <b>Form Pendaftaran</b>")
        return redirect('ppdb:form')
    
    if request.method == "POST":
        form = UpdateFormulirForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UpdateFormulirForm(instance=data)
        context = {
            'form': form,
        }
    return render(request, 'ppdb/form.html', context)

# @login_required(login_url="ppdb:login")
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def formulir(request):
#     '''fungsi menampilkan template formulir pendaftaran'''

#     nisn = request.user 
#     thn = TahunAjaran.objects.filter(status="Dibuka").last()

#     if request.method == "POST":
#         form = FormulirForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Formulir berhasil diajukan, silahkan tunggu verifikasi data")
#             return redirect('ppdb:form')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)
#             return redirect('ppdb:form')
    
#     form = FormulirForm(initial={'nisn':nisn, 'thn_ajaran':thn})
#     context = {
#         'page_title': 'Formulir PPDB | SMP Miftahul Falah Gandrungmangu',
#         'form': form,
#     }
#     return render(request, 'ppdb/form.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusDataPPDB(request, periode_id):
    '''fungsi hapus data periode ppdb'''

    pengaturan = TahunAjaran.objects.get(id_periode = periode_id)
    pengaturan.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:periode-ppdb")


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def editPeriode(request, periode_id):
    '''fungsi untuk merubah data periode ppdb'''

    if request.method == "POST":
        periode = TahunAjaran.objects.get(id_periode = periode_id)
        if periode != None:
            periode.tahun_ajaran = request.POST.get('tahun_ajaran')
            periode.tanggal_mulai = request.POST.get('tanggal_mulai')
            periode.tanggal_selesai = request.POST.get('tanggal_selesai')
            periode.status = request.POST.get('status')
            periode.save()
            messages.success(request, "Data Periode berhasil diperbarui!")   
            return redirect("ppdb:periode-ppdb")
    
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
            periode = TahunAjaran()
            periode.tahun_ajaran = request.POST.get('tahun_ajaran')
            periode.tanggal_mulai = request.POST.get('tanggal_mulai')
            periode.tanggal_selesai = request.POST.get('tanggal_selesai')
            periode.status = request.POST.get('status')
            periode.save()
            messages.success(request, "Data Periode berhasil ditambahkan!")
            return redirect("ppdb:periode-ppdb")
    else:
        return render(request, 'ppdb/modals/tambahPeriode.html')

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tahunAjaran(request):
    '''fungsi untuk menampilkan semua data periode ppdb'''

    pengaturan = TahunAjaran.objects.all().order_by('-id_thn_ajaran')

    if request.method == "POST":
        form = TahunAjaranForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "PPDB periode berhasil ditambahkan.")
            return redirect("ppdb:periode-ppdb")

    form = TahunAjaranForm()
    context = {
        'pengaturan': pengaturan,
        'heading': 'Tambah Periode PPDB',
        'button': 'Tambah',
        'form': form
    }
    return render(request, 'ppdb/TahunAjaran.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    '''fungsi menampilkan template dashboard'''

    total = Formulir.objects.all().count()
    terima = Formulir.objects.filter(verifikasi="Diterima").count()
    pending = Formulir.objects.filter(verifikasi="Pending").count()
    date = datetime.now().date()
    hari = Formulir.objects.filter(tgl_daftar__gt = date)


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

    peserta = Formulir.objects.all().order_by('-tgl_daftar')
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


# ============== ERRORS HANDLER ==============|
def error_404(request, exception):
    '''fungsi menampilkan template error 404'''
    return render(request, 'ppdb/404.html')

def error_505(request, exception):
    '''fungsi menampilkan template error 505'''
    return render(request, 'ppdb/505.html')