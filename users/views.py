from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.views import Response, status

from addresses.models import Address

from .models import User
from .serializers import UserSerializer, UserPatchSerializer, UserDeleteSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmOrOwner

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        address = self.request.data.pop("address")
        user = serializer.save()
        Address.objects.create(**address, user=user)

class UserUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrOwner]
    
    queryset = User.objects.all()
    serializer_class = UserPatchSerializer
    

class UserDeleteView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrOwner]
    
    queryset = User.objects.all()
    serializer_class = UserDeleteSerializer
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_204_NO_CONTENT)

