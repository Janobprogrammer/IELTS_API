from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TopicPartTwo
from .serializers import TopicSerializer


class TopicPartTwoListAPIView(APIView):
    def get(self, request):
        topics = TopicPartTwo.objects.prefetch_related("questions").all()
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
