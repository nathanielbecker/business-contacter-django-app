from django.contrib import admin
from .models import Initial_Borr_List_Page, DateTime, More_Data_Page
# from forms import barebonesAdminForm

# class ChoiceInline(admin.TabularInline):
#     model = Initial_Borr_List_Page
#     extra = 3

###from http://agiliq.com/blog/2014/08/passing-parameters-to-django-admin-action/ #####
from django.contrib.admin.helpers import ActionForm
from django import forms

from django.contrib.admin.models import LogEntry, CHANGE###need these to log the results of actions
from django.contrib.contenttypes.models import ContentType###need these to log the results of actions

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

def update_followup(modeladmin, request, queryset):# add businesses to FollowUp
    FollowUp = request.POST.get('FollowUp', True) #needs a default value
    FollowUp = bool(FollowUp)
    queryset.update(FollowUp=FollowUp)
    modeladmin.message_user(request, ("Will Contact these %d Businesses") % (queryset.count(),)) #, messages.SUCCESS
    ct = ContentType.objects.get_for_model(queryset.model) # for_model --> get_for_model
    for obj in queryset: # all the logging code comes from http://stackoverflow.com/questions/15404199/django-custom-admin-actions-logging
        LogEntry.objects.log_action( # log_entry --> log_action
            user_id = request.user.id,
            content_type_id = ct.pk,
            object_id = obj.pk,
            object_repr = obj.AtoZ_ID,
            action_flag = CHANGE, # actions_flag --> action_flag
            change_message = 'Added selections')
update_followup.short_description = "Contact these Businesses"

def update_followup_neg(modeladmin, request, queryset):# remove businesses from FollowUp
    FollowUp = request.POST.get('FollowUp', False) #needs a default value
    FollowUp = bool(FollowUp)
    queryset.update(FollowUp=FollowUp)
    modeladmin.message_user(request, ("Will No Longer Contact these %d Businesses") % (queryset.count(),)) #, messages.SUCCESS
    ct = ContentType.objects.get_for_model(queryset.model) # for_model --> get_for_model
    for obj in queryset: # all the logging code comes from http://stackoverflow.com/questions/15404199/django-custom-admin-actions-logging
        LogEntry.objects.log_action( # log_entry --> log_action
            user_id = request.user.id,
            content_type_id = ct.pk,
            object_id = obj.pk,
            object_repr = obj.AtoZ_ID,
            action_flag = CHANGE, # actions_flag --> action_flag
            change_message = 'Removed selections')
update_followup_neg.short_description = "Don't Contact these Businesses"

######

class barebones_admin(admin.ModelAdmin):
    # fields = ['AtoZ_ID', 'BankName', 'Business_Name', 'checkins', 'Est_Rent_Annual_Expense', 'executivedetails', 'final_phone', 'first_loan_date', 'Franchise', 'InitialInterestRate', 'last_loan_date', 'last_loan_end', 'likes', 'link', 'final_employees', 'Main_Line_of_Business', 'Manufacturer', 'NaicsDescription', 'num_loans', 'ownsrentsindicator', 'Physical_City', 'Physical_State', 'Physical_ZIP', 'rating', 'Revenue_Yr', 'review_count', 'Square_Footage', 'street3', 'sum_loans', 'Website', 'X2013_Employees', 'X2013_Revenue_Yr', 'final_yr_incorporated', 'url', 'Created', 'FindMoreData']
    list_display = ['FindMoreData', 'Business_Name', 'Est_Rent_Annual_Expense','website_link', 'final_employees', 'Main_Line_of_Business', 'ownsrentsindicator', 'street3', 'Physical_City', 'Physical_State', 'Physical_ZIP', 'Revenue_Yr']
    #this makes data display in spreadsheet format--note there's no "Created"
    search_fields = ["Business_Name",'Main_Line_of_Business']
    # action_form = UpdateActionForm
    actions = [update_findmoredata,update_findmoredata_neg]
    list_filter = ('ownsrentsindicator','Est_Rent_Annual_Expense','Physical_State')
    # form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin
    actions_on_top=True
    actions_on_bottom=False
    def has_add_permission(self, request):###removes big add button
        return False
    def website_link(self, obj):###highlight links--from http://stackoverflow.com/questions/1949248/how-to-add-clickable-links-to-a-field-in-django-admin
        return '<a href="%s">%s</a>' % (obj.Website, obj.Website)
    website_link.allow_tags = True

class ItemInline(admin.TabularInline):
    model = Initial_Borr_List_Page

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInline]

class More_data_page_admin(admin.ModelAdmin):
    fields = ["FollowUp",'AtoZ_ID', 'BankName', 'Business_Name', 'checkins', 'Est_Rent_Annual_Expense', 'executivedetails', 'final_phone', 'first_loan_date', 'Franchise', 'InitialInterestRate', 'last_loan_date', 'last_loan_end', 'likes', 'link', 'final_employees', 'Main_Line_of_Business', 'Manufacturer', 'NaicsDescription', 'num_loans', 'ownsrentsindicator', 'Physical_City', 'Physical_State', 'Physical_ZIP', 'rating', 'Revenue_Yr', 'review_count', 'Square_Footage', 'street3', 'sum_loans', 'Website', 'X2013_Employees', 'X2013_Revenue_Yr', 'final_yr_incorporated', 'url', 'Created']
    list_display = ['FollowUp', 'Business_Name', 'centile' , 'Main_Line_of_Business','Physical_City', 'num_loans', 'sum_loans', 'first_loan_date', 'last_loan_date', 'last_loan_end', 'InitialInterestRate', 'BankName', 'executivedetails', 'Revenue_Yr',  'final_employees', 'ownsrentsindicator', 'Square_Footage', 'Est_Rent_Annual_Expense', 'website_link', 'checkins', 'likes', 'facebook_link' ,'rating', 'review_count',  'yelp_link']####"BorrYelpLink","BorrYelpNumReviews",
    #this makes data display in spreadsheet format--note there's no "Created"
    search_fields = ["Business_Name",'Main_Line_of_Business','Physical_City']
    actions = [update_followup,update_followup_neg]
    list_filter = ('ownsrentsindicator', 'Square_Footage','Est_Rent_Annual_Expense','Physical_State')
    # form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin
    actions_on_top=True
    actions_on_bottom=False
    def has_add_permission(self, request):###removes big add button
        return False
    def yelp_link(self, obj):###highlight links--from http://stackoverflow.com/questions/1949248/how-to-add-clickable-links-to-a-field-in-django-admin
        return '<a href="%s">%s</a>' % (obj.url, obj.url)
    yelp_link.allow_tags = True
    # show_url.short_description = "Yelp Link"
    def facebook_link(self, obj):###highlight links--from http://stackoverflow.com/questions/1949248/how-to-add-clickable-links-to-a-field-in-django-admin
        return '<a href="%s">%s</a>' % (obj.link, obj.link)
    facebook_link.allow_tags = True
    def website_link(self, obj):###highlight links--from http://stackoverflow.com/questions/1949248/how-to-add-clickable-links-to-a-field-in-django-admin
        return '<a href="%s">%s</a>' % (obj.Website, obj.Website)
    website_link.allow_tags = True






admin.site.disable_action('delete_selected') #removes delete selected action--see http://stackoverflow.com/questions/1565812/the-default-delete-selected-admin-action-in-django

admin.site.register(Initial_Borr_List_Page,barebones_admin)
admin.site.register(DateTime, DateAdmin)
admin.site.register(More_Data_Page, More_data_page_admin)















# backup incase data migration goes shitty 1/29
# class barebones_admin(admin.ModelAdmin):
#     fields = ["FindMoreData","BorrName","BorrStreet","BorrState","BorrCity","BorrZip","BorrCounty","BorrPhoneNumber","BorrWebsite","BorrEmployees","BorrSales","BorrAge","BorrSICName","Created"]
#     list_display = ["FindMoreData","BorrName","BorrSICName","BorrStreet","BorrState","BorrCity","BorrState","BorrEmployees","BorrSales","BorrAge"]
#     #this makes data display in spreadsheet format--note there's no "Created"
#     search_fields = ["BorrName"]
#     # action_form = UpdateActionForm
#     actions = [update_findmoredata,update_findmoredata_neg]
#     list_filter = ('BorrSICName',)
#     # form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin
#     actions_on_top=True
#     actions_on_bottom=False
#     def has_add_permission(self, request):###removes big add button
#         return False
# class More_data_page_admin(admin.ModelAdmin):
#     fields = ["FollowUp","BorrName","BorrOwnerName","BorrYelpLink","BorrYelpNumReviews","BorrFacebookPage","BorrPreviousLender","BorrLastLoanDate","BorrLastLoanMaturity","BorrLoanType","BorrPhoneNumberVal","BorrLoanProb","BorrEmail","BorrWebsiteVal","BorrSquareft","BorrOwnRent"]
#     list_display = ["FollowUp","BorrName","BorrOwnerName","BorrYelpLink","BorrFacebookPage","BorrLastLoanDate","BorrPhoneNumberVal","BorrLoanProb","BorrWebsiteVal","BorrSquareft","BorrOwnRent"]####"BorrYelpLink","BorrYelpNumReviews",
#     #this makes data display in spreadsheet format--note there's no "Created"
#     search_fields = ["BorrName"]
#     actions = [update_followup,update_followup_neg]
#     list_filter = ('BorrOwnRent',"BorrSquareft")
#     # form = barebonesAdminForm ##customizes form, from http://stackoverflow.com/questions/5414853/customize-select-in-django-admin
#     actions_on_top=True
#     actions_on_bottom=False
#     def has_add_permission(self, request):###removes big add button
#         return False