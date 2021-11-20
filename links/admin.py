from django.contrib import admin

from links.models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('tiny_url', 'token')


admin.site.register(Link, LinkAdmin)
