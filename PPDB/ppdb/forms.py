from django import forms
from django.core.validators import RegexValidator
from . models import Formulir, TahunAjaran, DataAyah, DataIbu, DataWali, Berkas


# create your class here
class FormulirForm(forms.ModelForm):
    # override field
    nik = forms.CharField(
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )

    class Meta:
        model = Formulir
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
        }


class DataAyahForm(forms.ModelForm):
    nik_ayah = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    class Meta:
        model = DataAyah
        fields = "__all__"

class DataIbuForm(forms.ModelForm):
    nik_ibu = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    class Meta:
        model = DataIbu
        fields = "__all__"

class DataWaliForm(forms.ModelForm):
    nik_wali = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    class Meta:
        model = DataWali
        fields = "__all__"

class BerkasForm(forms.ModelForm):
    class Meta:
        model = Berkas
        fields = "__all__"


class UpdateFormulirForm(forms.ModelForm):
    class Meta:
        model = Formulir
        fields = "__all__"

        labels = {
            'verifikasi': 'Status Pendaftaran',
        }

        widgets = {
            'verifikasi': forms.TextInput(attrs={'readonly':'readonly'}),
            'no_pendaftaran': forms.TextInput(attrs={'readonly':'readonly'}),
            'alamat_siswa': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
        }


class EmailForm(forms.Form):
    # override file
    email = forms.EmailField()
    cc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(required=False, widget=forms.ClearableFileInput())
    message = forms.CharField(widget=forms.Textarea())


class TahunAjaranForm(forms.ModelForm):
    class Meta:
        model = TahunAjaran
        fields = "__all__"

        labels = {
            'tahun_ajaran': 'Tahun Ajaran',
            'status': 'Status',
            'tanggal_mulai': 'Tanggal Mulai',
            'tanggal_selesai': 'Tanggal Selesai',
        }
        
        widgets = {
            'tahun_ajaran': forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'2024/2025'}),
            'status': forms.Select(attrs={'class':'form-control form-control-sm'}),
            'tanggal_mulai': forms.DateInput(attrs={'class':'form-control form-control-sm', 'type':'date'}),
            'tanggal_selesai': forms.DateInput(attrs={'class':'form-control form-control-sm', 'type':'date'}),
        }