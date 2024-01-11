from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.core.mail import EmailMessage
from ppdb.forms.adminForms import EmailForm, TahunAjaranForm, ViewSiswaForm, ViewOrangTuaForm, ViewWaliForm, ViewBerkasForm
from ppdb.forms.pesertaForms import SiswaForm, OrangTuaForm, WaliForm, BerkasForm
from ppdb.models import Siswa,TahunAjaran, OrangTua
from ppdb.decorators import user_is_superuser

# ============== BACKEND VIEWS ADMIN (CONTROL MODEL SISWA) ==============|
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
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

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusData(request, id):
    '''fungsi hapus data peserta ppdb'''

    peserta = Siswa.objects.get(id_siswa=id)
    peserta.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:data-pendaftar")

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def verifikasiTolak(request):
    '''fungsi verifikasi data siswa'''

    if request.method == "POST":
        peserta = Siswa.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.verifikasi = request.POST.get('verifikasi')
            peserta.save()
            messages.success(request, "Siswa ditolak, silahkan kirim email untuk intruksi selanjutnya!")
            return redirect("ppdb:view-data")
        
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def verifikasiSiswa(request):
    '''fungsi verifikasi data siswa'''

    # verif data
    if request.method == "POST":
        siswa = Siswa.objects.get(id_siswa=Siswa.objects.get('id_siswa'))
        if siswa != None:
            siswa.verifikasi = request.POST.get('verifikasi')
            siswa.save()
            messages.success(request, "Siswa terverifikasi, silahkan kirim email untuk interuksi selanjutnya")

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @user_is_superuser
def viewData(request, id_siswa):
    '''fungsi menampilkan detail data peserta'''

    # get data with reverse queryset
    siswa = Siswa.objects.filter(id_siswa=id_siswa).first()
    ortu = siswa.ortu
    wali = siswa.wali
    berkas = siswa.berkas


    siswa = ViewSiswaForm(instance=siswa)
    ortu = ViewOrangTuaForm(instance=ortu)
    wali = ViewWaliForm(instance=wali)
    berkas = ViewBerkasForm(instance=berkas)
    context = {
        'siswa': siswa,
        'ortu': ortu,
        'wali': wali,
        'berkas': berkas,
    }
    return render(request, 'ppdb/viewData.html', context)   

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataDiterima(request):
    '''fungsi menampilkan data peserta berdasarkan data peserta diterima'''

    peserta = Siswa.objects.filter(verifikasi="Diterima").order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataDiterima.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataPendaftar(request):
    '''fungsi menampilkan semua data pendaftar'''

    peserta = Siswa.objects.all().order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataPendaftar.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusDataPPDB(request, periode_id):
    '''fungsi hapus data periode ppdb'''

    pengaturan = TahunAjaran.objects.get(id_periode = periode_id)
    pengaturan.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:periode-ppdb")


# ============== BACKEND VIEWS ADMIN (CONTROL MODEL TAHUN AJARAN) ==============|
@login_required(login_url="users:login")
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
    
@login_required(login_url="users:login")
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

@login_required(login_url="users:login")
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
    return render(request, 'ppdb/tahunAjaran.html', context)