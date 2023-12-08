from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from . models import Peserta


# create your class here
class UserRegistraionForm(UserCreationForm):
    # Override Fields in user_model
    email = forms.EmailField(
        help_text='Dimohon untuk memasukan email yang aktif', required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder':'example@gmail.com'})
    )
    username = forms.CharField(
        validators= [RegexValidator(r'^[\d]*$', message="NISN, hanya angka yg diizinkan")],
        widget = forms.TextInput(attrs={'maxlength':'10', 'placeholder':'NISN'}),
        label= 'NISN',
        help_text = 'Nomor NISN akan dijadikan username login anda.'
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Nama Depan'}),
        label='Nama Depan'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Nama Belakang'}),
        label="Nama Belakang"
    )
    
   
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(UserRegistraionForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
    

class PesertaForm(forms.ModelForm):
    # override field
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
            'alamat_ayah': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'alamat_ibu': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'alamat_wali': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
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
            'alamat_ayah': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'alamat_ibu': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
            'alamat_wali': forms.Textarea(attrs={'rows':'2', 'placeholder':'Alamat lengkap tempat tinggal sekarang', 'class':'col-md-12'}),
        }