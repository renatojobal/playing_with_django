from django.contrib import admin
from .models import UserChild

@admin.register(UserChild)
class UserChild(admin.ModelAdmin):

    list_display = ('pk', 'username', 'birthday',)
    list_display_links = ('pk', 'username',)
    list_editable = ('birthday',)

    #search_fields = ()

    #list_filter = ()