from rest_framework import generics

from .models import Program
from .serializers import ProgramSerializers


class ProgramListView(generics.ListAPIView):
    serializer_class = ProgramSerializers
    queryset = Program.objects.all()


class ProgramDetailView(generics.RetrieveAPIView):
    serializer_class = ProgramSerializers
    queryset = Program.objects.all()
