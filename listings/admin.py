from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'team_realtor')
    list_display_links = ('id', 'title')
    # filter box in team_realtor
    list_filter = ('team_realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city',
                     'state', 'zipcode', 'price')  # search in listings
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
