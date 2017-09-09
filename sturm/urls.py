from __future__ import absolute_import, unicode_literals

from django.conf.urls.static import static
from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [

    url(r'^admin/', include(wagtailadmin_urls)),

    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^books/', decorator_include(login_required, 'books.urls', namespace="books")),
    url(r'^techs/', decorator_include(login_required, 'techs.urls', namespace="techs")),
    url(r'^projects/', decorator_include(login_required, 'projects.urls', namespace="projects")),
    url(r'^lessons/', decorator_include(login_required, 'lessons.urls', namespace="lessons")),
    url(r'^students/', decorator_include(login_required, 'students.urls', namespace="students")),

    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', login_required(search_views.search), name='search'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:

    url(r'^', login_required(TemplateView.as_view(template_name='index.html')), name="home"),

    url(r'', decorator_include(login_required, wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
