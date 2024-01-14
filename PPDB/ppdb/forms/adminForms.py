from django import forms
from ppdb.models import TahunAjaran, Siswa, OrangTua, Wali, Berkas

# ============== BACKEND FORMS ADMIN ==============|
class EmailForm(forms.Form):
    email = forms.EmailField()
    cc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(required=False, widget=forms.ClearableFileInput())
    message = forms.CharField(widget=forms.Textarea())

# Forms for control tahun ajaran
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
            'tanggal_mulai': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type':'date'}),
            'tanggal_selesai': forms.TextInput(attrs={'class':'form-control form-control-sm', 'type':'date'}),
        }

# Disable all field from models
class ModelAllDisabledFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        '''This mixin to ModelForm disables all fields. Useful to have detail view based on model'''
        super().__init__(*args, **kwargs)
        form_fields = self.fields
        for key in form_fields.keys():
            form_fields[key].disabled = True

# Forms for control data siswa
class ViewSiswaForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'

        widgets = {
            'alamat': forms.Textarea(attrs={'rows':'2'}),
        }

class ViewOrangTuaForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = OrangTua
        fields = '__all__'

class ViewWaliForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Wali
        fields = '__all__'

class ViewBerkasForm(ModelAllDisabledFormMixin, forms.ModelForm):
    class Meta:
        model = Berkas
        fields = '__all__'

