#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django import forms
from taggit.models import Tag

# class StatusForm(forms.Form):
#     STATUS_CHOICES = [('no', 'Еще не читал'),
#                       ('inprog', 'Сейчас читаю'),
#                       ('yes', 'Уже прочитал')]
#     status = forms.MultipleChoiceField(
#         choices=STATUS_CHOICES,
#         widget=Select,
#     )
from techs.models import Tech


class BookSelectForm(forms.Form):
    LANG_CHOICES = [('en', 'Английский'),
                    ('ru', 'Русский')]
    LANG_CHOICES += [('any', 'Любые')]
    languages = forms.MultipleChoiceField(
        label="Языки",
        choices=LANG_CHOICES,
    )

    TECH_CHOICES = [(tech.title, tech.title) for tech in Tech.objects.all()]
    TECH_CHOICES += [('any', 'Любые')]
    techs = forms.MultipleChoiceField(
        label="Технологии",
        choices=TECH_CHOICES,
    )

    TAG_CHOICES = [(tag.slug, tag.name.title()) for tag in Tag.objects.all()]
    TAG_CHOICES += [('any', 'Любые')]
    tags = forms.MultipleChoiceField(
        label="Тэги",
        choices=TAG_CHOICES,
    )
