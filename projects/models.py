from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch import index

# from techs.models import Tech
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel


class Project(Page):
    parent_page_types = ['projects.ProjectIndex']

    github_url = models.URLField(blank=True)
    description = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('github_url'),
        InlinePanel('techs', label="Used technologies"),
        InlinePanel('students', label="Used technologies"),
    ]

    def __str__(self):
        return self.title


class ProjectStudentRelationship(models.Model):
    project = ParentalKey(Project, related_name='students')
    student = models.ForeignKey('students.Student')

    recommend = models.CharField(max_length=20, default="no")
    status = models.CharField(max_length=20, default="no")

    panels = [
        FieldPanel('recommend'),
        FieldPanel('status'),
        SnippetChooserPanel('student'),
    ]


class ProjectTechRelationship(models.Model):
    project = ParentalKey(Project, related_name='techs')
    tech = models.ForeignKey('techs.Tech')

    panels = [
        PageChooserPanel('tech', 'techs.Tech'),
    ]

class ProjectIndex(Page):
    subpage_types = ['projects.Project']