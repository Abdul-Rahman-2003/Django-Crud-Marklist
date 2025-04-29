from django import forms
from batman.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['stotal', 'sgrade']
