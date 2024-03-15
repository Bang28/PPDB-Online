from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.core.mail import EmailMessage
from ppdb.forms.adminForms import EmailForm, TahunAjaranForm, ViewPesertaForm, ViewPrestasiForm, ViewNilaiRaportForm, ViewBerkasForm
from ppdb.models import Peserta,TahunAjaran
from ppdb.decorators import user_is_superuser
from django.http import Http404, HttpResponse, FileResponse
from ppdb.renderers import render_to_pdf
import os
from django.conf import settings


# ============== BACKEND VIEWS ADMIN (CONTROL MODEL SISWA) ==============|
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def unduhFile(request, path):
    # file_path = os.path.join(settings.MEDIA_ROOT, path)
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/pdf")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return response
    # raise Http404
    # ext = os.path.basename(path).split('.')[-1].lower()
    # # cannot be used to download py, db and sqlite3 files.
    # if ext not in ['py', 'db',  'sqlite3']:
    #     response = FileResponse(open(path, 'rb'))
    #     response['content_type'] = "application/octet-stream"
    #     response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(path)
    #     return response
    # else:
    #     raise Http404
    try:
        response = FileResponse(open(path, 'rb'))
        response['content_type'] = "application/pdf"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(path)
        return response
    except Exception:
        raise Http404

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def exportPDF(request, id_peserta):
    siswa = Peserta.objects.get(id_peserta=id_peserta)
    ortu = siswa.ortu 
    wali = siswa.wali
    context = {
        'siswa': siswa,
        'ortu': ortu,
        'wali': wali,
    }
    response =  render_to_pdf('ppdb/export/pdf.html', context)
    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Formulir_{siswa.nama}.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response

@login_required(login_url="users:login")
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

    peserta = Peserta.objects.get(id_peserta=id)
    peserta.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect("ppdb:data-pendaftar")

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def verifikasiSiswa(request):
    '''fungsi verifikasi data siswa'''

    # verif data
    if request.method == "POST":
        siswa = Peserta.objects.get(id_peserta=request.POST.get('id_peserta'))
        if siswa != None:
            siswa.verifikasi = request.POST.get('verifikasi')
            siswa.save()
            messages.success(request, "Siswa terverifikasi, silahkan kirim email untuk interuksi selanjutnya")
            return redirect('ppdb:data-pendaftar')

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def viewData(request, id_peserta):
    '''fungsi menampilkan detail data peserta'''

    # get data with reverse queryset
    peserta = Peserta.objects.get(id_peserta=id_peserta)
    # cek atribut objek
    if hasattr(peserta, 'raport'):
        raport = peserta.raport 
        if hasattr(peserta, 'berkas'):
            berkas = peserta.berkas 
        else:
            berkas = None
            messages.info(request, 'peserta belum melengkapi berkas!')
            return redirect('ppdb:data-pendaftar')
    else:
        raport = None
        messages.info(request, 'peserta belum melengkapi data orangtua!')
        return redirect('ppdb:data-pendaftar')
    
    peserta = ViewPesertaForm(instance=peserta)
    raport = ViewNilaiRaportForm(instance=raport)
    berkas = ViewBerkasForm(instance=berkas)
    context = {
        'peserta': peserta,
        'raport': raport,
        'berkas': berkas,
    }
    return render(request, 'ppdb/forms/viewData.html', context)   

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataDiterima(request):
    '''fungsi menampilkan data peserta berdasarkan data peserta diterima'''

    peserta = Peserta.objects.filter(verifikasi="Diterima").order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataDiterima.html', context)


@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def dataPendaftar(request):
    '''fungsi menampilkan semua data pendaftar'''

    peserta = Peserta.objects.all().order_by('-tgl_daftar')
    context = {
        'peserta': peserta,
    }
    return render(request, 'ppdb/tables/dataPendaftar.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_is_superuser
def hapusDataPPDB(request, periode_id):
    '''fungsi hapus data periode ppdb'''

    pengaturan = TahunAjaran.objects.get(id_thn_ajaran = periode_id)

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
        periode = TahunAjaran.objects.get(id_thn_ajaran = periode_id)
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
    return render(request, 'ppdb/tables/tahunAjaran.html', context)