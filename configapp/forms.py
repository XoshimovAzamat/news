import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Categories, News


# class NewForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Yangilik nomi',
#                             widget=forms.TextInput(attrs={"class":"form-control"}))
#     context = forms.CharField(label="Yangilik haqida", required=False,
#                             widget=forms.Textarea(attrs={"class":"form-control",
#                                                             "rows": 5 }))
#     is_bool= forms.BooleanField(label="Nashr etish", initial=True)
#
#     category= forms.ModelChoiceField(empty_label="Qaysi tur?", label="Yangilik turi", queryset=Categories.objects.all(),
#                                      widget=forms.Select(attrs={"class":"form-control"}))
#

class NewForm(forms.ModelForm):

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'context', 'is_bool', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'row': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match(r'\d', title):
                raise ValidationError("Title raqam bo`lmasin!")
            return title
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model  = User
        fields = ('uesrname', 'password')