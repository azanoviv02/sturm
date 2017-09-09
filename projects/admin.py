from django.contrib import admin

from projects.models import Project
# from students.models import StudentProjectRelationship
# from techs.models import ProjectTechRelationship


# class StudentInline(admin.TabularInline):
#     model = StudentProjectRelationship


# class TechInline(admin.TabularInline):
#     model = ProjectTechRelationship


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'github_url', 'description']}),
    ]
    list_filter = ['title']
    search_fields = ['title']
    inlines = [
        # StudentInline,
        # TechInline,
    ]


admin.site.register(Project, ProjectAdmin)
