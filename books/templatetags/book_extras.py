from django import template

register = template.Library()


@register.inclusion_tag('books/extended_book_tags.html')
def extended_book_tags(book):
    return {'book': book}
