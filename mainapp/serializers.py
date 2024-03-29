from rest_framework import serializers
from .models import Program, NewsModel, InstructionModel, UrlModel


class ProgramSerializers(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'


class NewsModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = NewsModel
        fields = '__all__'


class InstructionModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = InstructionModel
        fields = '__all__'

class UrlModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = UrlModel
        fields = '__all__'