from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.core.mail import EmailMessage
from ppdb.forms import EmailForm
from ppdb.models import Siswa
from ppdb.decorators import user_is_superuser

# ============== BACKEND ==============|
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

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusData(request, id):
    '''fungsi hapus data peserta ppdb'''

    peserta = Siswa.objects.get(id_siswa=id)
    peserta.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:data-pendaftar")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def tolakForm(request):
    '''fungsi menginput nilai dari template viewData'''

    if request.method == "POST":
        peserta = Siswa.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.Keterangan = request.POST.get('Keterangan')
            peserta.save()
            messages.success(request, "Siswa ditolak, silahkan kirim balasan ke peserta")
            return redirect("ppdb:view-data")
        
@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def terimaForm(request):
    '''fungsi menginput nilai dari template viewData'''

    if request.method == "POST":
        peserta = Siswa.objects.get(id = request.POST.get('id'))
        if peserta != None:
            peserta.Keterangan = request.POST.get('Keterangan')
            peserta.save()
            messages.success(request, "Siswa diterima, silahkan kirim balasan ke peserta")
            return redirect("ppdb:data-diterima")

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def viewData(request, id):
    '''fungsi menampilkan detail data peserta'''

    peserta = Siswa.objects.get(id=id)
    if peserta != None:
        return render(request, 'ppdb/viewData.html', {'peserta': peserta})


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataDiterima(request):
    '''fungsi menampilkan data peserta berdasarkan data peserta diterima'''

    peserta = Siswa.objects.filter(verifikasi="Diterima").order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataDiterima.html', context)


@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataPendaftar(request):
    '''fungsi menampilkan semua data pendaftar'''

    peserta = Siswa.objects.all().order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataPendaftar.html', context)