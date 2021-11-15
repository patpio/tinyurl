from django.urls import path

from links import views

app_name = 'links'

urlpatterns = [
    path('create/', views.CreateLink.as_view(), name='create_link'),
    path('list/', views.LinkListView.as_view(), name='link_list'),
    path('<int:pk>/', views.LinkDetailView.as_view(), name='link_detail'),
    path('delete/<int:pk>', views.DeleteLink.as_view(), name='delete_link'),
]
