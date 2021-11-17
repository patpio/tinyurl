from django.contrib import admin

from links.models import Link


class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('tiny_url',)


admin.site.register(Link, LinkAdmin)
