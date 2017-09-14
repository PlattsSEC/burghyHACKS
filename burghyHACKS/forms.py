from django.contrib.auth.models import User
from django import forms

class userForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True, help_text='Pick something fancy. Like coolguy1616.')
    email = forms.EmailField(max_length=50, required=True, help_text="We'll never share your email with anyone else.")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']

    def __init__(self, *args, **kwargs):
        super(userForm, self).__init__(*args, **kwargs)
        # Adds form-control class to the fields for bootstrap
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })