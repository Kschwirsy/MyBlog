from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
		url(r'^about', 'blog.views.about'),
        url(r'^$', 'blog.views.index'),
        url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
        url(r"^add_comment/(\d+)/$", "add_comment"),
)

