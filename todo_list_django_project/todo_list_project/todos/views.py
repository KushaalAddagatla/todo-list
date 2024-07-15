# from rest_framework import viewsets
# from .models import Todo
# from .serializers import TodoSerializer

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer





from rest_framework import viewsets, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
