from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'duty': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'join_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'max': '9999-12-31'}),
            'leave_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'max': '9999-12-31'}),
            'photo': forms.FileInput(attrs={'class': 'd-none', 'onchange': 'setPhotoImage(event);'}),
            'status': forms.CheckboxInput(attrs={'class': 'd-none'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'nickname', 'department', 'duty',
            'position', 'phone', 'email', 'join_date',
            'leave_date', 'photo', 'status'
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'duty': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'join_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'max': '9999-12-31'}),
            'leave_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'max': '9999-12-31'}),
            'photo': forms.FileInput(attrs={'class': 'd-none', 'onchange': 'setPhotoImage(event);'}),
            'status': forms.CheckboxInput(attrs={'class': 'd-none'}),
        }
