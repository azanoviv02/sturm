from django.db import models
from django.db.models import CharField
from django.db.models import ManyToManyField
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsearch import index
from django.utils.encoding import python_2_unicode_compatible
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from wagtail.wagtailsnippets.models import register_snippet

from books.ru_taggit import RuTaggedItem


class Book(Page):
    parent_page_types = ['books.BookIndex']

    author = CharField(max_length=200, blank=False, null=False)
    description = RichTextField(blank=True)
    language = models.ForeignKey(
        'books.Language',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    lessons = ManyToManyField('lessons.Lesson', through='lessons.LessonBookRelationship')

    tags = TaggableManager(through=RuTaggedItem, blank=True)

    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('description', classname="full"),
        SnippetChooserPanel('language'),
        DocumentChooserPanel('file'),
        InlinePanel('techs', label="Mentioned technologies"),
        InlinePanel('students', label="Students"),
        FieldPanel('tags'),
    ]

    def __str__(self):
        return self.name


@register_snippet
@python_2_unicode_compatible
class Language(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    slug = models.CharField(max_length=20, null=False, blank=False)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name


class BookStudentRelationship(models.Model):
    book = ParentalKey(Book, related_name='students')
    student = models.ForeignKey('students.Student')

    recommend = models.CharField(max_length=20, default="no")
    status = models.CharField(max_length=20, default="no")

    panels = [
        SnippetChooserPanel('student'),
        FieldPanel('recommend'),
        FieldPanel('status'),
    ]


class BookTechRelationship(models.Model):
    book = ParentalKey(Book, related_name='techs')
    tech = models.ForeignKey('techs.Tech')

    panels = [
        PageChooserPanel('tech', 'techs.Tech'),
    ]


class BookIndex(Page):
    subpage_types = ['books.Book']