from django.conf.urls import url
from . import views
app_name = 'HotelApp'

urlpatterns = [
    url('^$', views.Index.as_view(),name='index'),
    url('^table/$', views.Table.as_view(),name='table'),
    url('^create/$', views.Create.as_view(),name='create'),
    url (r'^table/(?P<pk>\d+)/$',views.Detail.as_view(),name='detail')
]