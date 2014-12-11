from django import forms
from .models import barebones_CRUD
from django.contrib import admin


class barebones_CRUDForm(forms.ModelForm):
    class Meta:
        model = barebones_CRUD

####customize form labeling, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin
class barebonesAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(barebonesAdminForm, self).__init__(*args, **kwargs)
        self.fields['tags'].label = 'Custom Label'
#######