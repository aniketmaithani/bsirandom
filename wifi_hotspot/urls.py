# -*- coding: utf-8 -*-
"""Root url routering file.

You should put the url config in their respective app putting only a
refernce to them here.
"""

# Third Party Stuff
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

# Wifi Hotspot  Stuff
from wifi_hotspot.base import views as base_views
from wifi_hotspot.wifi_hotspot.views import (
    GeneratePasswordView, redirect_to_homepage)

from .routers import router

handler500 = base_views.server_error

# Top Level Pages
# ==============================================================================
urlpatterns = [
    url(r'^$', redirect_to_homepage, name="home"),
    url(r'^login/$', TemplateView.as_view(template_name='login.html'), name="login"),
    url(r'^profile/$', GeneratePasswordView.as_view(), name="profile"),
    # Your stuff: custom urls go here
]

urlpatterns += [

    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        base_views.root_txt_files, name='root-txt-files'),

    # Rest API
    url(r'^api/', include(router.urls)),

    # Browsable API
    url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),

    # Django Admin
    url(r'^{}/'.format(settings.DJANGO_ADMIN_URL), include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.API_DEBUG:
    urlpatterns += [
        # Browsable API
        url(r'^api/auth-n/', include('rest_framework.urls', namespace='rest_framework')),
    ]

if settings.DEBUG:
    from django.views import defaults as dj_default_views
    from django.urls import get_callable

    # debug toolbar
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

    # Livereloading
    urlpatterns += [url(r'^devrecargar/',
                        include('devrecargar.urls', namespace='devrecargar'))]

    urlpatterns += [
        url(r'^400/$', dj_default_views.bad_request,
            kwargs={'exception': Exception("Bad Request!")}),
        url(r'^403/$', dj_default_views.permission_denied,
            kwargs={'exception': Exception("Permission Denied!")}),
        url(r'^403_csrf/$', get_callable(settings.CSRF_FAILURE_VIEW)),
        url(r'^404/$', dj_default_views.page_not_found,
            kwargs={'exception': Exception("Not Found!")}),
        url(r'^500/$', handler500),
    ]
