from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, filters

from .models import LEVEL_CHOICES, Program

User = get_user_model()


class LevelFilter(FilterSet):
    level = filters.MultipleChoiceFilter(choices=LEVEL_CHOICES, initial=None)

    class Meta:
        model = Program
        fields = ("level",)