from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class Student(AbstractUser):
    books = models.ManyToManyField('books.Book', through='books.BookStudentRelationship')
    projects = models.ManyToManyField('projects.Project', through='projects.ProjectStudentRelationship')
    techs = models.ManyToManyField('techs.Tech', through='techs.TechStudentRelationship')
