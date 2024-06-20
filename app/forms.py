from user.admin import UserCreationForm
from django import forms
from user.models import CustomUser
from .models import Application, MyPersonDetail, MyPerson


class UserRegisterForm(UserCreationForm):
    required_css_class = 'form-group'

    class Meta:
        model = CustomUser
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    fields = (email, password)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )


class UserApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = (
            "email",
            "first_name",
            "last_name",
            "why_you",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )


class AddMyPerson(forms.ModelForm):

    class Meta:
        model = MyPerson
        fields = (
            'first_name',
            'last_name',
            'age',
            'gender',
            'photo',
            'majority',
            'short_description',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )


class AddMyPersonDetail(forms.ModelForm):

    class Meta:
        model = MyPersonDetail
        fields = (
            'person',
            'full_description',
            'quote',
            'financial_state'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )


class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = MyPerson
        fields = (
            'first_name',
            'last_name',
            'age',
            'gender',
            'photo',
            'majority',
            'short_description',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )


class PersonDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = MyPersonDetail
        fields = (
            'full_description',
            'quote',
            'financial_state'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {'class': 'custom-form'}
            )
