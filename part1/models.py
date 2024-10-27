from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Question(models.Model):
    topic = models.ForeignKey(Topic, related_name="questions", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
