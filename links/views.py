from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView

from links.models import Link


class CreateLink(CreateView):
    model = Link
    fields = ['url']
    template_name = 'links/create_link.html'

    def get_success_url(self):
        return reverse_lazy('links:link_detail', kwargs={'pk': self.object.pk})


class LinkDetailView(DetailView):
    model = Link
    template_name = 'links/link_detail.html'
    context_object_name = 'link'


class LinkListView(ListView):
    model = Link
    template_name = 'links/link_list.html'
    context_object_name = 'links'


class DeleteLink(DeleteView):
    model = Link
    template_name = 'links/delete_link.html'
    success_url = reverse_lazy('links:link_list')
