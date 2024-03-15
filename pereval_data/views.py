from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import *
from .serializers import PerevalSerializer


class PerevalCreateViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.filter(id=1)
    serializer_class = PerevalSerializer

    def get_queryset(self):
        return PerevalAdded.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 200,
                'message': '',
                'id': serializer.data.get('id')
            }
        elif status.HTTP_500_INTERNAL_SERVER_ERROR:
            response_data = {
                'status': 500,
                'message': 'Ошибка подключения к базе данных',
                'id': serializer.data.get('id')
            }
        elif status.HTTP_400_BAD_REQUEST:
            response_data = {
                'status': 400,
                'message': 'Неверный запрос',
                'id': serializer.data.get('id')
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
