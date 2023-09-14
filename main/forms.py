from django import forms


class AddPostFormMassag(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    telefon = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))




class AddPostFormTravel(forms.Form):
    name_t = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    telefon_t = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'placeholder': 'Телефон'}))
