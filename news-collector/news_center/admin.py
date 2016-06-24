from django.contrib import admin

# Register your models here.
from models import News


class NewsAdmin(admin.ModelAdmin):  # ,'dis_pros__bizcode'
    list_display = ('title', 'site', 'n_abs')
    # search_fields = ['title']

admin.site.register(News, NewsAdmin)
