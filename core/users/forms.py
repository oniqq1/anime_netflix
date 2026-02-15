from django.contrib.auth.password_validation import validate_password
from django.forms.models import ModelForm
from django import forms
from django.contrib.auth.models import User



class RegisterModel(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password' , "confirm_password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        try:
            if password or confirm_password:

                if password != confirm_password:
                    raise forms.ValidationError(
                        "Password and Confirm Password do not match"
                    )

                if len(password) < 8:
                    raise forms.ValidationError("Password must be at least 8 characters long")

                validate_password(password)
                return cleaned_data
        except forms.ValidationError as e:
                raise forms.ValidationError(e.messages)

    def email_clean(self):
        email = self.cleaned_data.get('email')
        if not email.endswith(end=['@gmail.com',"@yahoo.com","@example.com"]):
            raise forms.ValidationError("Email must be from the domains '@gmail.com' , '@yahoo.com' or '@example.com'")

        if email in User.objects.values_list('email', flat=True):
            raise forms.ValidationError("Email is already in use")

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")


        try:

            if username and password:
                try:
                    user = User.objects.get(username=username)
                    if not user.check_password(password):
                        raise forms.ValidationError("Invalid password")

                except User.DoesNotExist:
                    raise forms.ValidationError("Invalid username")

        except forms.ValidationError as e:
            raise forms.ValidationError(e.messages)

        return cleaned_data

    def get_user(self):
        username = self.cleaned_data.get("username")
        return User.objects.get(username=username)