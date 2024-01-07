from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from ppdb.decorators import user_is_superuser
from ppdb.models import TahunAjaran
from ppdb.forms import TahunAjaranForm
from django.contrib import messages


# ============== BACKEND ==============|
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
    return render(request, 'ppdb/tahunAjaran.html', context)