from rest_framework import generics, permissions
from .models import Heart
from .permissions import IsOwner

from .serializers import HeartSerializer


class HeartList(generics.ListCreateAPIView):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer

    def get_queryset(self):
        user = self.request.user
        return Heart.objects.filter(owner=user)

    def perform_create(self, serializer):
        """
        Set owner of of heart
        """
        serializer.save(owner=self.request.user)


class HeatDetail(generics.RetrieveUpdateAPIView):
    queryset = Heart.objects.all()
    serializer_class = HeartSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
