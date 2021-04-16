from rest_framework import serializers
from .models import Questions


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('id','title', 'desc', 'tags')
