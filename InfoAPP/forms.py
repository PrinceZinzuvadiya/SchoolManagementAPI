from django import forms
from .models import principal, faculty

class principalform(forms.ModelForm):
    class Meta:
        model=principal
        fields='__all__'

class facultyform(forms.ModelForm):
    class Meta:
        model=faculty
        fields='__all__'
        