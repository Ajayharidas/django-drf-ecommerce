from .models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets
from rest_framework.response import Response


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
