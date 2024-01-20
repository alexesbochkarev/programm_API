from rest_framework import generics
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from .filters import LevelFilter
from .models import Program, NewsModel, InstructionModel, UrlModel
from .serializers import ProgramSerializers, NewsModelSerializers, InstructionModelSerializers, UrlModelSerializers


class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LevelFilter

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
    queryset = NewsModel.objects.all()


class NewsDetailView(generics.RetrieveAPIView):
    serializer_class = NewsModelSerializers
    queryset = NewsModel.objects.all()


class InstructionListView(generics.ListAPIView):
    serializer_class = InstructionModelSerializers
    queryset = InstructionModel.objects.all()


class InstructionDetailView(generics.RetrieveAPIView):
    serializer_class = InstructionModelSerializers
    queryset = InstructionModel.objects.all()


class UrlListView(generics.ListAPIView):
    serializer_class = UrlModelSerializers
    queryset = UrlModel.objects.all()


class UrlDetailView(generics.RetrieveAPIView):
    serializer_class = UrlModelSerializers
    queryset = UrlModel.objects.all()
