from django.shortcuts import render, redirect
from ppdb.models import TahunAjaran, Peserta, Prestasi, NilaiRaport, Berkas
from ppdb.forms.pesertaForms import PesertaForm, PrestasiForm, NilaiRaportForm, BerkasForm, UpdatePesertaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# ============== BACKEND VIEWS PESERTA (UPDATE) ==============|
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateBerkas(request, id_peserta):
    '''fungsi update data berkas'''
        
    # get data berkas by id 
    berkas = Berkas.objects.get(id_berkas=id_peserta)
        
    if request.method == "POST":
        form = BerkasForm(request.POST, request.FILES, instance=berkas)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan tunggu verifikasi data dari pihak sekolah & cek email anda untuk melihat hasil pendaftaran!")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:update-berkas')
    
    form = BerkasForm(instance=berkas)
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Berkas:',
        'step': 'Step 3 - 3',
        'dm_active': 'active',
        'datadiri': ['active', 'done'],
        'ortu': ['active', 'done'],
        'wali': ['active', 'done'],
        'berkas': 'active',
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)


@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateNilaiRaport(request, id_peserta):
    '''fungsi update data data ortu'''

    # cek data siswa
    data = Peserta.objects.filter(nisn=request.user).get(nisn=request.user.id)

    # get data ibu by id 
    nilai = NilaiRaport.objects.get(id_nilai_raport=id_peserta)
    
    # get data berkas by filler 
    berkas = Berkas.objects.filter(peserta=data).first()
    
    if request.method == "POST":
        form = NilaiRaportForm(request.POST, request.FILES, instance=nilai)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan perbarui data berikut jika diperlukan!")
            return redirect('ppdb:update-berkas', id_peserta=berkas.id_berkas)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:update-data-nilai')
    
    form = NilaiRaportForm(instance=nilai)
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Nilai Raport:',
        'step': 'Step 2 - 3',
        'dm_active': 'active',
        'nilai_active': 'active',
        'datadiri': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updatePeserta(request, id_peserta):
    '''fungsi update data peserta'''

    # cek data siswa
    try:
        data = Peserta.objects.filter(nisn=request.user).get(nisn=id_peserta)
    except Peserta.DoesNotExist:
        data = None
        messages.info(request, f"Tidak ada data yang cocok, silahkan isi data terlebih dahulu di <b>Form Pendaftaran</b>")
        return redirect('ppdb:data-peserta')
    
    if data.verifikasi != "Pending":
        messages.info(request, 'data yang sudah diverifikasi tidak dapat dirubah!')
        return redirect('ppdb:dashboard')

    # get data ortu by filter
    nilai = NilaiRaport.objects.filter(peserta=data).first()
    
    if request.method == "POST":
        form = UpdatePesertaForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan perbarui data berikut jika diperlukan!")
            return redirect('ppdb:update-data-nilai', id_peserta=nilai.id_nilai_raport)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:update-data-peserta')
    
    form = UpdatePesertaForm(instance=data)
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Form Peserta:',
        'step': 'Step 1 - 3',
        'dm_active': 'active',
        'active': 'active',
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)


# ============== BACKEND VIEWS PESERTA (CREATE) ==============|
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def berkas(request):
    '''fungsi menampilkan form berkas'''

    # cek data siswa
    # siswa = Siswa.objects.filter(nisn=request.user).get(nisn=request.user.id)
    if Berkas.objects.filter(peserta__nisn=request.user.id).exists():
        messages.info(request, 'Anda sudah terdaftar di PPDB tahun ini!')
        return redirect('ppdb:dashboard')

    # get data siswa by filter
    peserta = Peserta.objects.filter(nisn=request.user).first()
    
    if request.method == "POST":
        form = BerkasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data anda sudah lengkap, silahkan tunggu verifikasi data dari pihak sekolah! & cek email anda untuk melihat hasil pendaftaran")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-berkas')
    
    # inisialisasi form
    form = BerkasForm(initial={'peserta':peserta})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Berkas:',
        'step': 'Step 3 - 3',
        'side_active': 'active',
        'berkas_active': 'active',
        'datadiri': ['active', 'done'],
        'ortu': ['active', 'done'],
        'wali': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def nilaiRaport(request):
    '''fungsi menampilkan form data nilai raport'''

    # cek data siswa
    if NilaiRaport.objects.filter(peserta__nisn=request.user.id).exists():
        return redirect('ppdb:data-berkas')

    peserta = Peserta.objects.filter(nisn=request.user).first()
    
    if request.method == "POST":
        form = NilaiRaportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data nilai Raport berhasil disimpan, silahkan lanjut lengkapi data berikut!")
            return redirect('ppdb:data-berkas')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-nilai')
    
    # inisialisasi form
    form = NilaiRaportForm(initial={'peserta':peserta})
    context = {
        'page_title': 'Peserta PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Nilai Raport:',
        'step': 'Step 2 - 3',
        'side_active': 'active',
        'nilai_active': 'active',
        'datadiri': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def peserta(request):
    '''fungsi menampilkan form data peserta'''

    # cek data siswa
    if Peserta.objects.filter(nisn=request.user).exists():
        return redirect('ppdb:data-nilai')

    nisn = request.user 
    thn = TahunAjaran.objects.filter(status="Dibuka").last()

    if request.method == "POST":
        form = PesertaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data peserta berhasil disimpan, silahkan lanjut lengkapi data berikut!")
            return redirect('ppdb:data-nilai')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-peserta')
    
    # inisialisasi form
    form = PesertaForm(initial={'nisn':nisn, 'thn_ajaran':thn})
    context = {
        'page_title': 'Peserta PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Peserta:',
        'step': 'Step 1 - 3',
        'side_active': 'active',
        'active': 'active',
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)