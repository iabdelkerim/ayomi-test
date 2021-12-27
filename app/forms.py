from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from .models import *

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmation de Mot de Passe', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirmation de Mot de passe'}))
    
    class Meta:
        model = MyUser
        fields = ('__all__')

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas !")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        return user

class registerForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    
    #password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmation de Mot de Passe', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirmation de Mot de passe'}))
    
    class Meta:
        model = MyUser
        fields = ('last_name','first_name','email','password','password2')
        widgets = {
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Dulot'}),
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Julien'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Adresse Mail'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Mot de Passe'})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas !")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        
        if commit:
            user.save()
        return user


class UserLoginForm(forms.ModelForm):


    class Meta:
        model  =  MyUser
        fields =  ('email', 'password')
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Adresse Mail'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Mot de Passe'})
        }
               
    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field in (self.fields['email'],self.fields['password']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean(self):
        if self.is_valid():

            email = self.cleaned_data.get('email')
            password = self.cleaned_data.get('password')
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Invalid Login')


class ProfileUpdateform(forms.ModelForm):
    """
      Updating User Info
    """

    
    class Meta:
        model  = MyUser
        fields = ('last_name','first_name','email')
        widgets = {
            'last_name':forms.TextInput(attrs={'class':'form-control','id':'last_name'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','id':'first_name'}),
            'email':forms.TextInput(attrs={'class':'form-control','id':'email'}),
                   
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(ProfileUpdateform, self).__init__(*args, **kwargs)
        for field in (self.fields['last_name'],self.fields['first_name'],self.fields['email']):
            field.widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = MyUser.objects.exclude(pk = self.instance.pk).get(email=email)
            except MyUser.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)



class EmailChangeform(forms.ModelForm):
    """
      Updating User Info
    """

    
    class Meta:
        model  = MyUser
        fields = ['email']
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control','id':'email'}),
                   
        }

    def __init__(self, *args, **kwargs):
        """
          specifying styles to fields 
        """
        super(EmailChangeform, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control '})

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = MyUser.objects.exclude(pk = self.instance.pk).get(email=email)
            except MyUser.DoesNotExist:
                return email
            raise forms.ValidationError("Email '%s' already in use." %email)


