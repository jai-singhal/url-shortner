from django.contrib import admin
from .models import UrlShortner
# Register your models here.

class CustomUrlShortnerAdmin(admin.ModelAdmin):
    pass
    # list_display = ('',)
    # list_filter = ('',)
    # # inlines = [
    # #     Inline,
    # # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


admin.site.register(UrlShortner, CustomUrlShortnerAdmin)
