from django.urls import path
from .views import TopicPartTwoListAPIView


urlpatterns = [
    path("topics/", TopicPartTwoListAPIView.as_view()),
]
