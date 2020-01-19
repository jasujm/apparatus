# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.static import serve

admin.autodiscover()

urlpatterns = [
    url(r"^sitemap\.xml$", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    url(r"^taggit_autosuggest/", include("taggit_autosuggest.urls")),
]

urlpatterns += i18n_patterns(
    url(r"^admin/", admin.site.urls), url(r"^", include("cms.urls")),  # NOQA
)

# This is only needed when using runserver.
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
        [
            path("__debug__/", include(debug_toolbar.urls)),
            url(
                r"^media/(?P<path>.*)$",
                serve,
                {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
            ),
        ]
        + staticfiles_urlpatterns()
        + urlpatterns
    )
