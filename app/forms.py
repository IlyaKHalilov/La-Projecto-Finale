from user.admin import UserCreationForm
from django import forms
from user.models import CustomUser


class UserRegisterForm(UserCreationForm):
    required_css_class = 'form-group'
    # email = forms.EmailField(
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'example@exmaple.com'}
    #     )
    # )
    # password1 = forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите пароль'
    #     }
    # )
    # password2 = forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите пароль'
    #     }
    # )

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
