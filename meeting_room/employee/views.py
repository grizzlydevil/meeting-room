from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from .serializers import EmployeeSerializer
from .models import Employee


class CreateEmployee(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.get(user=self.request.user)
