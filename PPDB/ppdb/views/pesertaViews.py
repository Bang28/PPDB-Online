from django.shortcuts import render, redirect
from ppdb.models import TahunAjaran, Siswa, OrangTua, Wali, Berkas
from ppdb.forms.pesertaForms import SiswaForm, OrangTuaForm, WaliForm, BerkasForm, UpdateSiswaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# ============== BACKEND VIEWS PESERTA (UPDATE) ==============|
@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateBerkas(request, id_siswa):
    '''fungsi update data berkas'''
        
    # get data berkas by id 
    berkas = Berkas.objects.get(id_berkas=id_siswa)
        
    if request.method == "POST":
        form = BerkasForm(request.POST, request.FILES, instance=berkas)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan tunggu verifikasi data dari pihak sekolah!")
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
        'step': 'Step 4 - 4',
        'dm_active': 'active',
        'datadiri': ['active', 'done'],
        'ayah': ['active', 'done'],
        'ibu': ['active', 'done'],
        'wali': ['active', 'done'],
        'berkas': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateWali(request, id_siswa):
    '''fungsi update data data wali'''

    # cek data siswa
    data = Siswa.objects.filter(nisn=request.user).get(nisn=request.user.id)
    
    # get data wali by id 
    wali = Wali.objects.get(id_wali=id_siswa)
    
    # get data berkas by filler 
    berkas = Berkas.objects.filter(siswa=data).first()
    
    if request.method == "POST":
        form = WaliForm(request.POST, request.FILES, instance=wali)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan perbarui data berikut jika diperlukan!")
            return redirect('ppdb:update-berkas', id_siswa=berkas.id_berkas)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:update-data-wali')
    
    form = WaliForm(instance=wali)
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Wali:',
        'step': 'Step 3 - 4',
        'dm_active': 'active',
        'wali_active': 'active',
        'datadiri': ['active', 'done'],
        'ortu': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateOrangtua(request, id_siswa):
    '''fungsi update data data ortu'''

    # cek data siswa
    data = Siswa.objects.filter(nisn=request.user).get(nisn=request.user.id)

    # get data ibu by id 
    ortu = OrangTua.objects.get(id_ortu=id_siswa)
    
    # get data wali by filler
    wali = Wali.objects.filter(siswa=data).first()
    
    if request.method == "POST":
        form = OrangTuaForm(request.POST, request.FILES, instance=ortu)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan perbarui data berikut jika diperlukan!")
            return redirect('ppdb:update-data-wali', id_siswa=wali.id_wali)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:update-data-ortu')
    
    form = OrangTuaForm(instance=ortu)
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Orang Tua:',
        'step': 'Step 2 - 4',
        'dm_active': 'active',
        'ortu_active': 'active',
        'datadiri': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateDatadiri(request, id_siswa):
    '''fungsi update data diri siswa'''

    # cek data siswa
    try:
        data = Siswa.objects.filter(nisn=request.user).get(nisn=id_siswa)
    except Siswa.DoesNotExist:
        data = None
        messages.info(request, f"Tidak ada data yang cocok, silahkan isi data terlebih dahulu di <b>Form Pendaftaran</b>")
        return redirect('ppdb:data-diri')

    # get data ortu by filler
    ortu = OrangTua.objects.filter(siswa=data).first()
    
    if request.method == "POST":
        form = UpdateSiswaForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data diperbarui, silahkan perbarui data berikut jika diperlukan!")
            return redirect('ppdb:update-data-ortu', id_siswa=ortu.id_ortu)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:update-data-diri')
    
    form = UpdateSiswaForm(instance=data)
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Diri:',
        'step': 'Step 1 - 4',
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
    if Berkas.objects.filter(siswa__nisn=request.user.id).exists():
        messages.info(request, 'Anda sudah terdaftar di PPDB tahun ini!')
        return redirect('ppdb:dashboard')

    # get data siswa by filter
    siswa = Siswa.objects.filter(nisn=request.user).first()
    
    if request.method == "POST":
        form = BerkasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data anda sudah lengkap, silahkan tunggu verifikasi data dari pihak sekolah!")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-berkas')
    
    # inisialisasi form
    form = BerkasForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Berkas:',
        'step': 'Step 4 - 4',
        'side_active': 'active',
        'berkas_active': 'active',
        'datadiri': ['active', 'done'],
        'ortu': ['active', 'done'],
        'wali': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def wali(request):
    '''fungsi menampilkan form data wali'''

    # cek data siswa
    # siswa = Siswa.objects.filter(nisn=request.user).get(nisn=request.user.id)
    if Wali.objects.filter(siswa__nisn=request.user.id).exists():
        return redirect('ppdb:data-berkas')

    siswa = Siswa.objects.filter(nisn=request.user).first()
    
    if request.method == "POST":
        form = WaliForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Wali disimpan, silahkan lanjut lengkapi data berikut!")
            return redirect('ppdb:data-berkas')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-wali')
    
    # inisialisasi form
    form = WaliForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Wali:',
        'step': 'Step 3 - 4',
        'side_active': 'active',
        'wali_active': 'active',
        'datadiri': ['active', 'done'],
        'ortu': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def orangTua(request):
    '''fungsi menampilkan form data ortu'''

    # cek data siswa
    # siswa = Siswa.objects.filter(nisn=request.user).get(nisn=request.user.id)
    if OrangTua.objects.filter(siswa__nisn=request.user.id).exists():
        return redirect('ppdb:data-wali')

    siswa = Siswa.objects.filter(nisn=request.user).first()
    
    if request.method == "POST":
        form = OrangTuaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Orang Tua disimpan, silahkan lanjut lengkapi data berikut!")
            return redirect('ppdb:data-wali')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-ortu')
    
    # inisialisasi form
    form = OrangTuaForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Orang Tua:',
        'step': 'Step 2 - 4',
        'side_active': 'active',
        'ortu_active': 'active',
        'datadiri': ['active', 'done'],
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)

@login_required(login_url="users:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataDiri(request):
    '''fungsi menampilkan data diri'''

    # cek data siswa
    if Siswa.objects.filter(nisn=request.user).exists():
        return redirect('ppdb:data-ortu')

    nisn = request.user 
    thn = TahunAjaran.objects.filter(status="Dibuka").last()

    if request.method == "POST":
        form = SiswaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Datadiri disimpan, silahkan lanjut lengkapi data berikut!")
            return redirect('ppdb:data-ortu')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-diri')
    
    # inisialisasi form
    form = SiswaForm(initial={'nisn':nisn, 'thn_ajaran':thn})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'h3': 'Data Diri:',
        'step': 'Step 1 - 4',
        'side_active': 'active',
        'active': 'active',
    }
    return render(request, 'ppdb/forms/pesertaForm.html', context)