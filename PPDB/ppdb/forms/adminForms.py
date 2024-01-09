from django import forms
from ppdb.models import TahunAjaran

# ============== BACKEND FORMS ADMIN ==============|
class EmailForm(forms.Form):
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