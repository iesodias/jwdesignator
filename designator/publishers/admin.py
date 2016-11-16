from django.contrib import admin
from designator.publishers.models import Publisher

class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'group', 'gender')
    search_fields = ('name', 'designation', 'group', 'gender')

admin.site.register(Publisher, PublisherModelAdmin)