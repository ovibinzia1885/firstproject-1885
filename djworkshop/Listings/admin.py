from django.contrib import admin
from.models import Listing
from.models import Realtor

class Listingadmin(admin.ModelAdmin):

    class Meta:
        model=Listing
    list_display = ('id','title','address','price','sqft','garage','des2','photo_main','realtor','is_published',)
    list_display_links = ['id','title']
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','address','price',)

admin.site.register(Listing,Listingadmin)





