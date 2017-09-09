#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from operator import and_

from django.db.models import Q
from django.urls import reverse
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView

from books.forms import BookSelectForm
from books.models import Book, BookStudentRelationship
from techs.models import Tech

always_true_criteria = ~Q(pk=None)

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'latest_book_list'

    def get_criteria_list(self):
        return [always_true_criteria]

    def get_status(self, book_list):
        connection_list = self.request.user.bookstudentrelationship_set.all()

        for book in book_list:
            for connection in connection_list:
                if book.id == connection.book.id:
                    book.status = connection.status
                    book.recommend = connection.recommend
            if not hasattr(book, 'status'):
                book.status = 'no'
            if not hasattr(book, 'recommend'):
                print("here")
                book.recommend = 'no'
            book.recommend = "recommend-" + str(book.recommend)
            print(book.recommend)

    def get_queryset(self):
        book_list = Book.objects \
            .filter(reduce(and_, self.get_criteria_list())) \
            .distinct()

        # tech_list = Tech.objects.all()
        # for tech in tech_list:
        #     print(tech)
        # TECH_CHOICES = [(tech.title.lower(), tech.title) for tech in Tech.objects.all()]
        # print(TECH_CHOICES)

        self.get_status(book_list)

        return book_list


class SpecificIndexView(IndexView):
    def get_criteria_list(self):
        languages = self.kwargs['languages'].split('*')
        if languages != ["any"]:
            lang_criteria = Q(language__slug__in=languages)
        else:
            lang_criteria = always_true_criteria

        techs = self.kwargs['techs'].split('*')
        if "any" not in techs:
            print("Getting tech criteria")
            tech_criteria = Q(techs__tech__title__in=techs)
        else:
            tech_criteria = always_true_criteria

        tags = self.kwargs['tags'].split('*')
        if "any" not in tags:
            tag_criteria = Q(tags__slug__in=tags)
        else:
            tag_criteria = always_true_criteria

        return [lang_criteria, tech_criteria, tag_criteria]


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'


class SelectorView(generic.FormView):
    template_name = 'books/selector.html'
    form_class = BookSelectForm

    def form_valid(self, form):
        delim = '*'
        self.kwargs['languages'] = delim.join(form.cleaned_data['languages'])
        self.kwargs['techs'] = delim.join(form.cleaned_data['techs'])
        self.kwargs['tags'] = delim.join(form.cleaned_data['tags'])
        return super(SelectorView, self).form_valid(form)

    def get_success_url(self):
        languages = self.kwargs['languages']
        techs = self.kwargs['techs']
        tags = self.kwargs['tags']
        return reverse(
            'books:specific_index',
            kwargs={
               'languages': languages,
               'techs': techs,
               'tags': tags
           }
        )


class StatusUpdateView(APIView):
    def post(self, request, format=None):
        book_id = request.data['book_id']
        new_status = request.data['new_status']

        print(new_status)

        student_id = self.request.user.id
        print("Student id: " + str(student_id))
        BookStudentRelationship.objects.update_or_create(student__pk=student_id,
                                                         book__pk=book_id,
                                                         defaults={
                                                             'student_id': student_id,
                                                             'book_id': book_id,
                                                             'status': new_status}
                                                         )

        return Response("Status updated successfully")
