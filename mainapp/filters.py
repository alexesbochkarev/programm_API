from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, filters

from .models import Program

User = get_user_model()


class LevelFilter(FilterSet):
    level = filters.MultipleChoiceFilter(choices=Program.LEVEL_CHOICES, initial=None)

    class Meta:
        model = Program
        fields = ("level",)