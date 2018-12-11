from django.conf.urls import url
from my_app import views

# template tagging
app_name = 'my_app'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^school/$', views.SchoolListView.as_view(), name='list'),
    # url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^school/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete')
]
