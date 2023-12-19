from django import forms
from django.core.validators import RegexValidator
from . models import Peserta, PeriodePPDB


# create your class here
class PesertaForm(forms.ModelForm):
    # override field in Peserta Model
    nik = forms.CharField(
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    nik_ayah = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    nik_ibu = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )
    nik_wali = forms.CharField(
        required=False,
        validators = [RegexValidator(r'^[\d]*$', message="NIK, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'16'}),
        label= 'NIK',
    )

    class Meta:
        model = Peserta
        fields = '__all__'

        labels = {
	        'thn_ajaran': 'Tahun Ajaran',
	        'nisn': 'NISN',
        }

        widgets = {
            'tgl_lahir': forms.DateInput(attrs={'type':'date'}),
            'tgl_lahir_ayah': forms.DateInput(attrs={'type':'date'}),
            'tgl_lahir_ibu': forms.DateInput(attrs={'type':'date'}),
            'tgl_lahir_wali': forms.DateInput(attrs={'type':'date'}),
            'Keterangan': forms.TextInput(attrs={'type':'hidden'}),
            'no_pendaftaran': forms.TextInput(attrs={'type':'hidden'}),
            'nisn': forms.TextInput(attrs={'type':'hidden'}),
            'thn_ajaran': forms.TextInput(attrs={'type':'hidden'}),
            'alamat_siswa': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'kip': forms.RadioSelect(attrs={'class':'btn-check'}),
            'pkh_kks': forms.RadioSelect(attrs={'class':'btn-check'}),
            'jenis_kelamin': forms.RadioSelect(attrs={'class':'btn-check'}),
        }

    # super function
    def __init__(self, *args, **kwargs):
        super(PesertaForm, self).__init__(*args, **kwargs)
        self.fields['agama'].choices = [("", "Pilih agama")] + list(self.fields['agama'].choices)[1:]


class UpdatePesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = "__all__"

        labels = {
            'Keterangan': 'Status Pendaftaran',
        }

        widgets = {
            'Keterangan': forms.TextInput(attrs={'readonly':'readonly'}),
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


class PeriodePPDBForm(forms.ModelForm):
    class Meta:
        model = PeriodePPDB
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