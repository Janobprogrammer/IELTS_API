from rest_framework import serializers
from .models import TopicPartTwo, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_part"]


class TopicSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = TopicPartTwo
        fields = ["id", "title", "status", "question", "answer", "questions"]
