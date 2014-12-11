from django.contrib import admin
from .models import barebones_CRUD, DateTime
from forms import barebonesAdminForm


# class ChoiceInline(admin.TabularInline):
#     model = barebones_CRUD
#     extra = 3

###from http://agiliq.com/blog/2014/08/passing-parameters-to-django-admin-action/ #####
from django.contrib.admin.helpers import ActionForm
from django import forms

class UpdateActionForm(ActionForm):
    FollowUp = forms.BooleanField(required=False)
    FindMoreData = forms.BooleanField(required=False)
   

def update_followup(modeladmin, request, queryset):
    FollowUp = request.POST.get('FollowUp', True) #needs a default value
    FollowUp = bool(FollowUp)
    queryset.update(FollowUp=FollowUp)
    modeladmin.message_user(request, ("Successfully updated FollowUp for %d rows") % (queryset.count(),)) #, messages.SUCCESS
update_followup.short_description = "Contact These Businesses"


def update_findmoredata(modeladmin, request, queryset):
    FindMoreData = request.POST.get('FindMoreData', True) #needs a default value
    FindMoreData = bool(FindMoreData)
    queryset.update(FindMoreData=FindMoreData)
    modeladmin.message_user(request, ("Successfully updated FindMoreData for %d rows") % (queryset.count(),)) #, messages.SUCCESS
update_findmoredata.short_description = "Find More Information on These Businesses"

######

class barebones_admin(admin.ModelAdmin):
    fields = ["FollowUp","FindMoreData","name","BorrName","BorrStreet","BorrState","BorrCity","BorrZip","Created"]
    list_display = ["FollowUp","FindMoreData","name","BorrName","BorrStreet","BorrState","BorrCity","BorrZip"] #this makes data display in spreadsheet format #note there's no "Created"
    search_fields = ["name"]
    action_form = UpdateActionForm
    actions = [update_followup,update_findmoredata]
    list_filter = ('BorrZip',)
    form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin

class ItemInline(admin.TabularInline):
    model = barebones_CRUD

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInline]


admin.site.disable_action('delete_selected') #removes delete selected action--see http://stackoverflow.com/questions/1565812/the-default-delete-selected-admin-action-in-django

admin.site.register(barebones_CRUD,barebones_admin)
admin.site.register(DateTime, DateAdmin)

