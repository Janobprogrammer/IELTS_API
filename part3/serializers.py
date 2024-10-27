from rest_framework import serializers
from .models import TopicPartThree, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question", "answer"]


class TopicSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = TopicPartThree
        fields = ["id", "title", "status", "questions"]
