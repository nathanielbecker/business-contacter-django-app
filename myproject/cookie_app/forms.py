from django import forms
from .models import Initial_Borr_List_Page
from django.contrib import admin


class Initial_Borr_List_PageForm(forms.ModelForm):
    class Meta:
        model = Initial_Borr_List_Page

####customize form labeling, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin
class barebonesAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(barebonesAdminForm, self).__init__(*args, **kwargs)
        self.fields['tags'].label = 'Custom Label'
#######