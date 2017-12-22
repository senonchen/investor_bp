from django.contrib import admin

from .models import investor

class investorAdmin(admin.ModelAdmin):
    fields = ['realname','telephone','weixin','email','company','position','industry','investAmount','fields','stages','roles','ps']
    list_display = ('realname','position','industry','investAmount','fields','stages','company','ps',)
    search_fields = ['fields']
    
admin.site.register(investor, investorAdmin)
