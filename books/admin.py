from copy import deepcopy
from django.contrib import admin

from books.models import Book
# from students.models import StudentBookRelationship
# from techs.models import BookTechRelationship


# class StudentInline(admin.TabularInline):
#     model = StudentBookRelationship

# class TechInline(admin.TabularInline):
#     model = BookTechRelationship


class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ("title",
                       "author",
                       "description",
                       "file",
                       "language",
                       "tags")
        }),
    )
    list_display = ["title", 'author']
    list_filter = ['title']
    search_fields = ['title', 'author']
    inlines = [
        # StudentInline,
        # TechInline,
    ]


admin.site.register(Book, BookAdmin)
