from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

from links.models import Link


class HomeView(TemplateView):
    template_name = 'home/home.html'


class RedirectUrlView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_obj = get_object_or_404(Link, token=kwargs['token'])
        return url_obj.url
