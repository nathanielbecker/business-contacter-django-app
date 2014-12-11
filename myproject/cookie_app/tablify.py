import django_tables2 as tables
from .models import barebones_CRUD

class SimpleTable(tables.Table):
    class Meta:
        model = barebones_CRUD