from django.contrib import admin

from .models import Page, UserFileUpload

# This is use to add extra sections to the '/admin' directory.
admin.site.register(Page) # Registers page to the admin site
admin.site.register(UserFileUpload) # Registers file uploads to the admin site