from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


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
    

class UserProfileForm(forms.ModelForm): 
    email = forms.EmailField()
    
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'image',
        ]


class UserAddForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'is_superuser',
            'password1',
            'password2',
        ]