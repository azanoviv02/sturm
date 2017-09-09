from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, PageChooserPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks

import lessons
from books.models import Book
from lessons.blocks import CodeBlock


class Lesson(Page):
    parent_page_types = ['lessons.LessonIndex']

    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title", template='blocks/heading.html')),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock()),
        ('image', ImageChooserBlock()),
        ('video', EmbedBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('body'),
        InlinePanel('techs', label="Mentioned technologies"),
        InlinePanel('books', label="Mentioned books"),
        InlinePanel('related_article_links', label="Related links"),
    ]


class LessonRelatedArticleLink(Orderable):
    page = ParentalKey(Lesson, related_name='related_article_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]


class LessonTechRelationship(models.Model):
    lesson = ParentalKey(Lesson, related_name='techs')
    tech = models.ForeignKey('techs.Tech')

    panels = [
        PageChooserPanel('tech', 'techs.Tech'),
    ]


class LessonBookRelationship(models.Model):
    lesson = ParentalKey(Lesson, related_name='books')
    book = models.ForeignKey(Book)

    panels = [
        PageChooserPanel('book', 'books.Book'),
    ]


class LessonIndex(Page):
    subpage_types = ['lessons.Lesson']