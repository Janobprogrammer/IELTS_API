from django.db import models


class TopicPartTwo(models.Model):
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    topic = models.ForeignKey(TopicPartTwo, related_name="questions", on_delete=models.CASCADE)
    question_part = models.TextField()

    def __str__(self):
        return self.question_part
