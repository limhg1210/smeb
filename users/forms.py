from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreateForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }

    re_password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}))

    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'}),
            'join_date': forms.TextInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'leave_date': forms.TextInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'photo': forms.FileInput(attrs={'class': 'd-none', 'onchange': 'setPhotoImage(event);'}),
            'status': forms.CheckboxInput(attrs={'class': 'd-none'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if 'class' not in visible.field.widget.attrs.keys():
                visible.field.widget.attrs['class'] = 'form-control'

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password and re_password:
            if password != re_password:
                raise ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data["password"])
        if commit:
            instance.save()
        return instance


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'name', 'nickname', 'department', 'duty',
            'position', 'phone', 'email', 'join_date',
            'leave_date', 'photo', 'status'
        )

        widgets = {
            'join_date': forms.TextInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'leave_date': forms.TextInput(attrs={'type': 'date', 'max': '9999-12-31'}),
            'photo': forms.FileInput(attrs={'class': 'd-none', 'onchange': 'setPhotoImage(event);'}),
            'status': forms.CheckboxInput(attrs={'class': 'd-none'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if 'class' not in visible.field.widget.attrs.keys():
                visible.field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.data.get('photo_default') == 'true':
            instance.photo = 'default/profile_photo.png'
        if commit:
            instance.save()
        return instance
