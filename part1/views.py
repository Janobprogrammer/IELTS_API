from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Topic
from .serializers import TopicSerializer


class TopicListAPIView(APIView):
    def get(self, request):
        topics = Topic.objects.prefetch_related("questions").all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
