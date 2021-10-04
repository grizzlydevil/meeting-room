from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).first()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        self.check_object_permissions(self.request, queryset)
        return queryset
