from django.contrib import admin

from.models import Realtor

class realtoradmin(admin.ModelAdmin):

    class Meta:
        model = Realtor


    list_display = ('id',  'email', 'des1','is_mvp',)
    list_display_links = ('id',)
    list_filter = ('name',)
    search_fields = ( 'email', 'des1',)
    list_editable = ('is_mvp',)


admin.site.register(Realtor,realtoradmin)