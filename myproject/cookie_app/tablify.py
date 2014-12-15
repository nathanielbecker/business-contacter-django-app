import django_tables2 as tables
from .models import Initial_Borr_List_Page

class SimpleTable(tables.Table):
    class Meta:
        model = Initial_Borr_List_Page