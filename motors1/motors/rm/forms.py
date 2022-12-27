from django import forms
from django.db import models
from rm.models import *

class motorform(forms.ModelForm):
    class Meta:
        model=Motors
        fields='__all__'