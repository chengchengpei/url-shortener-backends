from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^$', views.LinkView.as_view(), name='link'),
    url(r'^(?P<code>\w+)$', views.LinkDetailView.as_view(), name='link_detail'),
]
