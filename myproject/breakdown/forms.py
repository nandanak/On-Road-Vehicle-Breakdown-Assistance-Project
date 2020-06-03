from django import forms
from breakdown.models import User, Profile
from django.forms.utils import ValidationError

class CustSignupForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    location = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=12)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    repeatpass = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('fullname','email','location','city','contact','username','password')

    def clean(self):
        cleaned_data =super(CustSignupForm, self).clean()
        fullname = cleaned_data.get("fullname")
        email = cleaned_data.get("email")
        location = cleaned_data.get("location")
        city = cleaned_data.get("city")
        contact = cleaned_data.get("contact")
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        repeatpass = cleaned_data.get("repeatpass")

        if password != repeatpass:
            raise forms.ValidationError(
                "Passwords don't match"
            )

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user

class ProfileForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    workshop = forms.CharField(max_length=100)
    location = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=12)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    repeatpass = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Profile
        fields = ('fullname','email','workshop','bio','location','city','contact','username','password')

#    def __init__(self, data, **kwargs):
#        initial = kwargs.get('initial', {})
#        data = {**initial, **data}
#        super().__init__(data, **kwargs)

    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        fullname = cleaned_data.get('fullname')
        email = cleaned_data.get('email')
        workshop = cleaned_data.get('workshop')
        special = cleaned_data.get('special')
        bio = cleaned_data.get('bio')
        location = cleaned_data.get('location')
        city = cleaned_data.get('city')
        contact = cleaned_data.get('contact')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        repeatpass = cleaned_data.get("repeatpass")

    def save(self):
        user = super().save(commit=False)
        user.save()
        return user

class MechSignupForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    workshop = forms.CharField(max_length=100)
    special = forms.CharField(max_length=100)
    bio = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=12)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    repeatpass = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('fullname','email','workshop','special','bio','location','city','contact','username','password')

    def clean(self):
        cleaned_data =super(MechSignupForm, self).clean()
        password = cleaned_data.get("password")
        repeatpass = cleaned_data.get("repeatpass")

        if password != repeatpass:
            raise forms.ValidationError(
                "Passwords don't match"
            )

    def save(self):
        user = super().save(commit=False)
        user.is_mechanic = True
        user.save()
        return user
