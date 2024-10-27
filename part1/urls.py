from django.urls import path
from .views import TopicListAPIView


urlpatterns = [
    path("topics/", TopicListAPIView.as_view()),
]
