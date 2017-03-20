# Third Party Stuff
from django.contrib import admin

from .models import PasswordGeneration


class PasswordGenerationAdmin(admin.ModelAdmin):

    '''
    Admin View for Complaints
    '''
    list_display = ('password_unique', 'created_at')
    list_filter = ('created_at',)
    search_fields = ['password_unique', 'created_at', ]

admin.site.register(PasswordGeneration, PasswordGenerationAdmin)
