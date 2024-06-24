# -*- coding: utf-8 -*-
"""
Main application Views
"""

from django.shortcuts import render, redirect

# URLS
from django.urls import reverse_lazy


# **************************
# *     Home Page View     *
# **************************
def home_page_redirect_view(request):
    """
    Provede presmerovani na zvolenou stranku ve strukture - nejcasteji simple manual page

    Je to obvykle jedinne View definovane na urovni aplikace/view.py jinak by se mela view definovat
    v ramci jednotlivych aplikacnich modulu z duvodu prenositelnosti jadra Asbd Like aplikaci mezi
    jednotlivymi specifickymi aplikacemi.

    @param request:
    @return:    response
    """
    response = redirect(reverse_lazy("common:home-page"))
    return response


def layout_test(request):
    from sharedlibrary.utils.menu import ViewMenu
    context = {
        "menu_right": ViewMenu(),
    }

    return render(request,
                  template_name='test_layout_page_template.html',
                  context=context)
