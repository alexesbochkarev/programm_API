from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, filters

from .models import LEVEL_CHOICES, Program, NewsModel, InstructionModel


User = get_user_model()


class ProgramLevelFilter(FilterSet):
    level = filters.MultipleChoiceFilter(choices=LEVEL_CHOICES, initial=None)

    class Meta:
        model = Program
        fields = ("level",)


class NewsLevelFilter(FilterSet):
    level = filters.MultipleChoiceFilter(choices=LEVEL_CHOICES, initial=None)

    class Meta:
        model = NewsModel
        fields = ("level",)


class InstructionLevelFilter(FilterSet):
    level = filters.MultipleChoiceFilter(choices=LEVEL_CHOICES, initial=None)

    class Meta:
        model = InstructionModel
        fields = ("level",)
