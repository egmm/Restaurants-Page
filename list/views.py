# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from models import Restaurant, MenuItem
from django.views import generic
from comments.models import Comment


class IndexView(generic.ListView):
    template_name = 'list/index.html'
    model = Restaurant

class MenuListView(generic.DetailView):
    model = Restaurant
    template_name = 'list/menuList.html'

    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all().filter(restaurant = context['object'].pk)
        return context
