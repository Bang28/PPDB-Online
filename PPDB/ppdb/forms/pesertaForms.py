from django import forms
from django.core.validators import RegexValidator
from ppdb.models import Peserta, Prestasi, NilaiRaport, Berkas


# ============== BACKEND FORMS PESERTA (UPDATE) ==============|
class UpdatePesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
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
class PesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
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
            'tlp_peserta': forms.TextInput(attrs={'class':'phone'}),
            'anak_ke': forms.TextInput(attrs={'type':'number'}),
        }

class PrestasiForm(forms.ModelForm):
    class Meta:
        model = Prestasi
        fields = '__all__'

        widgets = {
            'peserta': forms.TextInput(attrs={'type':'hidden'}),
        }


class NilaiRaportForm(forms.ModelForm):
    class Meta:
        model = NilaiRaport
        fields = '__all__'

        widgets = {
            'peserta': forms.TextInput(attrs={'type':'hidden'}),
        }

class BerkasForm(forms.ModelForm):
    class Meta:
        model = Berkas
        fields = '__all__'

        widgets = {
            'peserta': forms.TextInput(attrs={'type':'hidden'}),
        }