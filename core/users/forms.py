from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.forms import ModelForm


class RegisterModel(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ('@gmail.com', '@yahoo.com', '@example.com')
        if not email.endswith(allowed_domains):
            raise forms.ValidationError(
                "Email must be from '@gmail.com', '@yahoo.com' or '@example.com'"
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Passwords do not match")
            if len(password) < 8:
                raise forms.ValidationError("Password must be at least 8 characters long")
            validate_password(password)

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
            self.user = user

        return cleaned_data

    def get_user(self):
        return self.user
