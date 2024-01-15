from django import forms
from django.core.validators import RegexValidator
from ppdb.models import Siswa, OrangTua, Wali, Berkas


# ============== BACKEND FORMS PESERTA (UPDATE) ==============|
class UpdateSiswaForm(forms.ModelForm):
    # override field
    nik = forms.CharField(
        validators = [RegexValidator(r'^[\d]*$', message="Periksa kembali NIK anda!")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )

    class Meta:
        model = Siswa
        fields = "__all__"

        labels = {
            'verifikasi': 'Status Pendaftaran',
        }

        widgets = {
            'verifikasi': forms.TextInput(attrs={'type':'hidden'}),
            'no_pendaftaran': forms.TextInput(attrs={'type':'hidden'}),
            'nisn': forms.TextInput(attrs={'type':'hidden'}),
            'thn_ajaran': forms.TextInput(attrs={'type':'hidden'}),
            'alamat': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'jenis_kelamin': forms.RadioSelect(attrs={'class':'btn-check'}),
            'tgl_lahir': forms.TextInput(attrs={'type':'date'}),
        }


# ============== BACKEND FORMS PESERTA (CREATE) ==============|
class SiswaForm(forms.ModelForm):
    # override field
    nik = forms.CharField(
        validators = [RegexValidator(r'^[\d]*$', message="Periksa kembali NIK anda!")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )

    class Meta:
        model = Siswa
        fields = '__all__'

        labels = {
	        'thn_ajaran': 'Tahun Ajaran',
	        'nisn': 'NISN',
        }

        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type':'date'}),
            'verifikasi': forms.TextInput(attrs={'type':'hidden'}),
            'no_pendaftaran': forms.TextInput(attrs={'type':'hidden'}),
            'nisn': forms.TextInput(attrs={'type':'hidden'}),
            'thn_ajaran': forms.TextInput(attrs={'type':'hidden'}),
            'alamat': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'jenis_kelamin': forms.RadioSelect(attrs={'class':'btn-check'}),
            'no_hp': forms.TextInput(attrs={'class':'phone'})
        }

class OrangTuaForm(forms.ModelForm):
    nik_ayah = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="Periksa kembali NIK Ayah anda!")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK Ayah',
    )
    nik_ibu = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="Periksa kembali NIK Ibu anda!")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK Ibu',
    )
    class Meta:
        model = OrangTua
        fields = '__all__'

        widgets = {
            'tgl_lahir_ayah': forms.TextInput(attrs={'type':'date'}),
            'tgl_lahir_ibu': forms.TextInput(attrs={'type':'date'}),
            'siswa': forms.TextInput(attrs={'type':'hidden'}),
        }


class WaliForm(forms.ModelForm):
    nik_wali = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="Periksa kembali NIK Wali anda!")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    class Meta:
        model = Wali
        fields = '__all__'

        widgets = {
            'tgl_lahir_wali': forms.TextInput(attrs={'type':'date'}),
            'siswa': forms.TextInput(attrs={'type':'hidden'}),
        }

class BerkasForm(forms.ModelForm):
    class Meta:
        model = Berkas
        fields = '__all__'

        widgets = {
            'siswa': forms.TextInput(attrs={'type':'hidden'}),
        }