from django import forms
from django import forms
from Home.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"  

