from django.db import models
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from books.ru_taggit import RuTaggedItem


class Tech(Page):
    parent_page_types = ['techs.TechIndex']

    # connections
    projects = models.ManyToManyField('projects.Project', through='projects.ProjectTechRelationship')
    lessons = models.ManyToManyField('lessons.Lesson', through='lessons.LessonTechRelationship')
    books = models.ManyToManyField('books.Book', through='books.BookTechRelationship')

    # tags
    tags = TaggableManager(through=RuTaggedItem, blank=True)

    # content

    # off_page = models.URLField(blank=True)
    # off_docs = models.URLField(blank=True)

    # descriptions = RichTextField(blank=True)
    body = RichTextField(blank=True)
    logo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        # index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        # FieldPanel('off_page'),
        # FieldPanel('off_docs'),
        # FieldPanel('description', classname="full"),
        FieldPanel('tags'),
        ImageChooserPanel('logo_image'),
        InlinePanel('related_article_links', label="Related article links"),
        InlinePanel('related_video_links', label="Related video links"),
    ]

    def __str__(self):
        return self.title


class TechRelatedArticleLink(Orderable):
    page = ParentalKey(Tech, related_name='related_article_links')
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('description', classname="full"),
        FieldPanel('url'),
    ]


class TechRelatedVideoLink(Orderable):
    page = ParentalKey(Tech, related_name='related_video_links')
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    video = StreamField([
        ('video', EmbedBlock()),
    ], blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description', classname="full"),
        StreamFieldPanel('video'),
    ]


class TechStudentRelationship(models.Model):
    tech = ParentalKey(Tech, related_name='students')
    student = models.ForeignKey('students.Student')

    panels = [
        SnippetChooserPanel('student'),
    ]


class TechIndex(Page):
    subpage_types = ['techs.Tech']