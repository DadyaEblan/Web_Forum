from rest_framework import generics, viewsets
from .models import Author
from .permissions import AuthorPermission
from .serializers import AuthorRegisterSerializer


class AuthorRegisterViewSet(generics.CreateAPIView):
    serializer_class = AuthorRegisterSerializer


class AuthorCreateListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer


class AuthorRetrieveUpdateDestroyAPIView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer
    permission_classes = [AuthorPermission, ]
