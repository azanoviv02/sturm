from django.contrib import admin

from students.models import Student
    # StudentProjectRelationship


# class BookInline(admin.TabularInline):
#     model = StudentBookRelationship


# class ProjectInline(admin.TabularInline):
#     model = StudentProjectRelationship


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        # BookInline,
        # ProjectInline,
    ]


admin.site.register(Student, StudentAdmin)
