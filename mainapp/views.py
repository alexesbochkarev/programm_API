from rest_framework import generics
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ProgramLevelFilter, NewsLevelFilter, InstructionLevelFilter
from .models import Program, NewsModel, InstructionModel, UrlModel
from .serializers import ProgramSerializers, NewsModelSerializers, InstructionModelSerializers, UrlModelSerializers


class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProgramLevelFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return Program.objects.all()
            else:
                return Program.objects.filter(Q(level="A") | Q(level="B"))
        else:
            return Program.objects.filter(level="A")


class ProgramDetailView(generics.RetrieveAPIView):
    serializer_class = ProgramSerializers
    queryset = Program.objects.all()


class NewsListView(generics.ListAPIView):
    serializer_class = NewsModelSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NewsLevelFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return NewsModel.objects.all()
            else:
                return NewsModel.objects.filter(Q(level="A") | Q(level="B"))
        else:
            return NewsModel.objects.filter(level="A")


class NewsDetailView(generics.RetrieveAPIView):
    serializer_class = NewsModelSerializers
    queryset = NewsModel.objects.all()


class InstructionListView(generics.ListAPIView):
    serializer_class = InstructionModelSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstructionLevelFilter

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return InstructionModel.objects.all()
            else:
                return InstructionModel.objects.filter(Q(level="A") | Q(level="B"))
        else:
            return InstructionModel.objects.filter(level="A")


class InstructionDetailView(generics.RetrieveAPIView):
    serializer_class = InstructionModelSerializers
    queryset = InstructionModel.objects.all()


class UrlListView(generics.ListAPIView):
    serializer_class = UrlModelSerializers
    queryset = UrlModel.objects.all()


class UrlDetailView(generics.RetrieveAPIView):
    serializer_class = UrlModelSerializers
    queryset = UrlModel.objects.all()
