from rest_framework import serializers
from .models import Program


class ProgramSerializers(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'
