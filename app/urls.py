from django.conf.urls import url
# from django.views.generic.base import RedirectView
from . import views
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # url(r'^favicon\.ico$', RedirectView.as_view(url='static/favicon.ico', permanent=True)),
    url(r'^news$', views.news_list, name="news"),
    url(r'^news/(?P<id>[0-9]+)$', views.news_detail, name="news"),
    url(r'^case$', views.case_list, name="case"),
    url(r'^case/(?P<id>[0-9]+)$', views.case_detail, name="case"),
    url(r'^product$', views.product, name="product"),
    url(r'^about$', views.about, name="index"),
]

handler404 = 'page_not_found'
handler500 = 'app.views.server_error'
handler403 = 'app.views.forbidden'