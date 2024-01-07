from django.shortcuts import render, redirect
from ppdb.models import TahunAjaran, Siswa
from ppdb.forms import SiswaForm, DataAyahForm, DataIbuForm, DataWaliForm, BerkasForm, UpdateSiswaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# ============== BACKEND ==============|
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def berkas(request):
    '''fungsi menampilkan template Siswa datadiri'''

    siswa = Siswa.objects.filter(nisn=request.user)
    
    if request.method == "POST":
        form = BerkasForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berkas disimpan, silahkan lengkapi data berikut!")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:berkas')
    
    form = BerkasForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'active': 'active',
    }
    return render(request, 'ppdb/forms/singleForm.html', context)

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataWali(request):
    '''fungsi menampilkan template Siswa datadiri'''

    siswa = Siswa.objects.filter(nisn=request.user)
    
    if request.method == "POST":
        form = DataWaliForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Wali disimpan, silahkan lengkapi data berikut!")
            return redirect('ppdb:berkas')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-wali')
    
    form = DataWaliForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'active': 'active',
    }
    return render(request, 'ppdb/forms/singleForm.html', context)

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataIbu(request):
    '''fungsi menampilkan template Siswa datadiri'''

    siswa = Siswa.objects.filter(nisn=request.user)
    
    if request.method == "POST":
        form = DataIbuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Ibu disimpan, silahkan lengkapi data berikut!")
            return redirect('ppdb:data-wali')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-ibu')
    
    form = DataIbuForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'active': 'active',
    }
    return render(request, 'ppdb/forms/singleForm.html', context)

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataAyah(request):
    '''fungsi menampilkan template Siswa datadiri'''

    siswa = Siswa.objects.filter(nisn=request.user)
    
    if request.method == "POST":
        form = DataAyahForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Ayah disimpan, silahkan lengkapi data berikut!")
            return redirect('ppdb:data-ibu')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-ayah')
    
    form = DataAyahForm(initial={'siswa':siswa})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
        'active': 'active',
    }
    return render(request, 'ppdb/forms/singleForm.html', context)

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataDiri(request):
    '''fungsi menampilkan template Siswa datadiri'''

    nisn = request.user 
    thn = TahunAjaran.objects.filter(status="Dibuka").last()

    if request.method == "POST":
        form = SiswaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Datadiri disimpan, silahkan lengkapi data berikut!")
            return redirect('ppdb:data-ayah')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            return redirect('ppdb:data-diri')
    
    form = SiswaForm(initial={'nisn':nisn, 'thn_ajaran':thn})
    context = {
        'page_title': 'Siswa PPDB | SMP Miftahul Falah Gandrungmangu',
        'form': form,
    }
    return render(request, 'ppdb/forms/singleForm.html', context)

@login_required(login_url="ppdb:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dataMaster(request, pk):
    '''fungsi view data dan edit data master peserta berdasarkan request user'''

    try:
        data = Siswa.objects.filter(nisn=request.user).get(nisn=pk)
    except Siswa.DoesNotExist:
        data = None
        messages.info(request, f"Tidak ada data yang cocok, silahkan isi data terlebih dahulu di <b>Form Pendaftaran</b>")
        return redirect('ppdb:data-diri')
    
    if request.method == "POST":
        form = UpdateSiswaForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ppdb:dashboard')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UpdateSiswaForm(instance=data)
        context = {
            'form': form,
        }
    return render(request, 'ppdb/form.html', context)