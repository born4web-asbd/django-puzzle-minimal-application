"""
ASBD URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from minimalpuzzle.views import home_page_redirect_view, layout_test

# Error Views
from sharedlibrary.views import (SimpleBadPageURLView,
                                 UserConfiguratedHomepageRedirectView)


urlpatterns = [
    # ADMIN modul
    path('admin/', admin.site.urls, name='django-admin'),

    # HOME
    path('', UserConfiguratedHomepageRedirectView.as_view(), name='home-page'),

    # SHAREDLIBRARY modul
    path('common/', include("sharedlibrary.urls", namespace="common")),

    # ACCOUNTS modul
    path('accounts/', include("accounts.urls", namespace="accounts")),

    # CONTACTS modul
    path('contacts/', include("contacts.urls", namespace="contacts")),

    # TinyMCE WYSIWYG editor
    path('summernote/', include('django_summernote.urls')),

    # TEXTNOTE modul
    path('textnote/', include("textnote.urls", namespace="textnote")),

    # FEEDBACK modul
    path('feedback/', include("feedback.urls", namespace="feedback")),

    path('test-layout', layout_test, name="test-layout"),

    # BAD PAGE URL
    path('<str:bad_page_url>/', SimpleBadPageURLView.as_view(), name='bad-page-url'),
]
