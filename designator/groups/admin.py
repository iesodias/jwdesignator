from django.contrib import admin
from designator.groups.models import Group

class GroupModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'sup_group')
    search_fields = ('name','address', 'sup_group')

admin.site.register(Group, GroupModelAdmin)