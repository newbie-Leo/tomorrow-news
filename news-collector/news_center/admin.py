from django.contrib import admin

# Register your models here.
from models import News, NewsSite


class NewsAdmin(admin.ModelAdmin):  # ,'dis_pros__bizcode'
    list_display = ('title', 'b_type', 'site', 'n_abs')
    list_filter = ('b_type',)
    # search_fields = ['title']


class NewsSiteAdmin(admin.ModelAdmin):  # ,'dis_pros__bizcode'
    list_display = ('site_name', 'site_type')
    list_per_page = 10
    list_editable = ('site_type',)
    list_filter = ('site_type',)
    search_fields = ('site_name',)

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        if change:
            News.objects.filter(
                site=obj.site_name).update(b_type=obj.site_type)
        obj.save()


admin.site.register(News, NewsAdmin)
admin.site.register(NewsSite, NewsSiteAdmin)
