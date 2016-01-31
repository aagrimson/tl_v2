from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^newtest/$', views.newtest, name='newtest'),
    url(r'^updatetest/$', views.TestUpdate.as_view(), name='updatetest'),
    url(r'^listtest/$', views.TestListing.as_view(), name='listing'),
    url(r'^listtest/(?P<pk>\d+)/$', views.TestDetail.as_view(), name='detail'),

]


# urlpatterns = [
#     url(r'^$', views.home, name='home'),
#     url(r'^newtest/$', views.testsCreateView, name='newtest'),
#     url(r'^modifytest/$', views.testsUpdateView, name='modifytest'),

# ]