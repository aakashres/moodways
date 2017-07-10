from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': 'true',
        'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': 'true',
        'placeholder': 'Re-type Password'}))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control placeholder-no-fix'})

        self.fields["first_name"].widget.attrs.update(
            {'placeholder': 'First Name', 'required': 'true'})
        self.fields["last_name"].widget.attrs.update(
            {'placeholder': 'Last Name', 'required': 'true'})
        self.fields["username"].widget.attrs.update(
            {'placeholder': 'Username', 'required': 'true'})
        self.fields["email"].widget.attrs.update(
            {'placeholder': 'E-Mail', 'required': 'true'})

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")

        return password2


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'required': 'true',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-solid placeholder-no-fix',
        'required': 'true',
    }))

    class Meta:
        fields = [
            "username",
            "password",
        ]


class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['deleted_at', 'gallery']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DaysForm(forms.ModelForm):
    class Meta:
        model = Days
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['is_promotional'].widget.attrs.update({'class': ''})
        self.fields['place'].queryset = Place.objects.filter(
            deleted_at=None)
        self.fields['season'].queryset = Season.objects.filter(
            deleted_at=None)
        self.fields['day'].queryset = Days.objects.filter(
            deleted_at=None)
        self.fields['gallery'].queryset = Gallery.objects.filter(
            deleted_at=None)


class ItenaryForm(forms.ModelForm):
    class Meta:
        model = Itenary
        exclude = ['deleted_at', 'package']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['deleted_at', 'blog']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'style': 'width:300px;', 'placeholder': 'Your Name'})
        self.fields['email'].widget.attrs.update(
            {'style': 'width:300px;', 'placeholder': 'Your Email'})
        self.fields['body'].widget.attrs.update(
            {'style': 'width:700px;', 'placeholder': 'Your Experince'})


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        exclude = ['deleted_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields['parent'].queryset = Menu.objects.filter(
                deleted_at=None)


class SliderForm(forms.ModelForm):

    class Meta:
        model = Slider
        fields = [
            'file',
            'fileType',
            'label',
            'active',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['active'].widget.attrs.update({'class': ''})


class TrailerForm(forms.ModelForm):

    class Meta:
        model = Trailer
        exclude = ['deleted_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ['deleted_at', 'package']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields["discount_code"].widget.attrs.update({'required': 'true'})
        self.fields["travelDate"].widget.attrs.update(
            {'id': 'datepicker'})


class CouponForm(forms.ModelForm):
    validFrom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control datetimepicker',
        'required': 'true',
    }))
    validTo = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control datetimepicker',
        'required': 'true',
    }))

    class Meta:
        model = Coupon
        exclude = ['deleted_at', 'valid_to', 'valid_from']
        include = ['validFrom', 'validTo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        self.fields['package'].widget.attrs.update({'id': 'select-list'})
        self.fields['validFrom'].widget.attrs.update(
            {'class': 'datetimepicker form-control'})
        self.fields['validTo'].widget.attrs.update(
            {'class': 'datetimepicker form-control'})
