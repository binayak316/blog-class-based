from django.contrib import admin
from .models import POST

# Register your models here.

class POSTAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    # row ma dekhaune style
    list_filter = ('status',)
    # right side ma filter option for draft or published

    search_fields = ['title', 'Content']
    #     search button lyaunxa mathi
    prepopulated_fields = {
        'slug': ('title',)
    }
# this populated the slug if i created the title it automatically slugs the title look how interesting hehe

admin.site.register(POST,POSTAdmin)
