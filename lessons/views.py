# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from lessons.models import Lesson


class IndexView(generic.ListView):
    template_name = 'lessons/index.html'
    context_object_name = 'lesson_list'

    def get_queryset(self):
        """Return the last five published books."""
        return Lesson.objects.all()


class DetailView(generic.DetailView):
    model = Lesson
    template_name = 'lessons/detail.html'
