from django.contrib import admin
from .models import urun

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_date','isPublished')
    list_display_links = ('id','name')
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
    search_fields = ('name','description')
    list_per_page = 10

# Register your models here.
admin.site.register(urun, MovieAdmin)