from rest_framework import generics

from .models import Program, NewsModel, InstructionModel, UrlModel
from .serializers import ProgramSerializers, NewsModelSerializers, InstructionModelSerializers, UrlModelSerializers


class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializers
    queryset = Program.objects.all()


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
