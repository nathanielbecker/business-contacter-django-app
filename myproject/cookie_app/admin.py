from django.contrib import admin
from .models import Initial_Borr_List_Page, DateTime, More_Data_Page
from forms import barebonesAdminForm

# class ChoiceInline(admin.TabularInline):
#     model = Initial_Borr_List_Page
#     extra = 3

###from http://agiliq.com/blog/2014/08/passing-parameters-to-django-admin-action/ #####
from django.contrib.admin.helpers import ActionForm
from django import forms

# class UpdateActionForm(ActionForm): ###this produces little check boxes next to the action dropdown 
#     # FollowUp = forms.BooleanField(required=False)
#     FindMoreData = forms.BooleanField(required=False)
   

# def update_followup(modeladmin, request, queryset):
#     FollowUp = request.POST.get('FollowUp', True) #needs a default value
#     FollowUp = bool(FollowUp)
#     queryset.update(FollowUp=FollowUp)
#     modeladmin.message_user(request, ("Successfully updated FollowUp for %d rows") % (queryset.count(),)) #, messages.SUCCESS
# update_followup.short_description = "Contact These Businesses"

def update_findmoredata(modeladmin, request, queryset):# add businesses to FindMoreData
    FindMoreData = request.POST.get('FindMoreData', True) #needs a default value
    FindMoreData = bool(FindMoreData)
    queryset.update(FindMoreData=FindMoreData)
    modeladmin.message_user(request, ("Will Find More Information on these  %d Businesses") % (queryset.count(),)) #, messages.SUCCESS
update_findmoredata.short_description = "Find More Information on these Businesses"

def update_findmoredata_neg(modeladmin, request, queryset):# remove businesses from FindMoreData
    FindMoreData = request.POST.get('FindMoreData', False) #needs a default value 
    FindMoreData = bool(FindMoreData)
    queryset.update(FindMoreData=FindMoreData)
    modeladmin.message_user(request, ("Will No Longer Find More Information on these  %d Businesses") % (queryset.count(),)) #, messages.SUCCESS
update_findmoredata_neg.short_description = "Don't Find More Information on these Businesses"

######

class barebones_admin(admin.ModelAdmin):
    fields = ["FindMoreData","BorrName","BorrStreet","BorrState","BorrCity","BorrZip","BorrCounty","BorrPhoneNumber","BorrWebsite","BorrEmployees","BorrSales","BorrAge","BorrSICName","Created"]
    list_display = ["FindMoreData","BorrName","BorrSICName","BorrStreet","BorrState","BorrCity","BorrState","BorrEmployees","BorrSales","BorrAge"]
    #this makes data display in spreadsheet format--note there's no "Created"
    search_fields = ["BorrName"]
    # action_form = UpdateActionForm
    actions = [update_findmoredata,update_findmoredata_neg]
    list_filter = ('BorrSICName',)
    form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin

class ItemInline(admin.TabularInline):
    model = Initial_Borr_List_Page

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInline]

class More_data_page_admin(admin.ModelAdmin):
    fields = ["FollowUp","BorrName","BorrYelpLink","BorrYelpNumReviews","BorrFacebookPage","BorrPreviousLender","BorrLastLoanDate","BorrLastLoanMaturity","BorrLoanType","BorrPhoneNumberVal","BorrLoanProb","BorrEmail","BorrWebsiteVal","BorrSquareft","BorrOwnRent"]
    list_display = ["FollowUp","BorrName","BorrYelpLink","BorrYelpNumReviews","BorrFacebookPage","BorrPreviousLender","BorrLastLoanDate","BorrLastLoanMaturity","BorrLoanType","BorrPhoneNumberVal","BorrLoanProb","BorrEmail","BorrWebsiteVal","BorrSquareft","BorrOwnRent"]
    #this makes data display in spreadsheet format--note there's no "Created"
    search_fields = ["BorrName"]
    # action_form = UpdateActionForm
    # actions = [update_findmoredata,update_findmoredata_neg]
    list_filter = ('BorrOwnRent',)
    # form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin









admin.site.disable_action('delete_selected') #removes delete selected action--see http://stackoverflow.com/questions/1565812/the-default-delete-selected-admin-action-in-django

admin.site.register(Initial_Borr_List_Page,barebones_admin)
admin.site.register(DateTime, DateAdmin)
admin.site.register(More_Data_Page, More_data_page_admin)


