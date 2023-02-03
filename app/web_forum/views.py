from rest_framework import generics
from .permissions import ForumPermission, CommentPermission
from .serializers import ForumSerializer, CommentSerializer
from .models import Forum, Comment


class ForumViewSet(generics.ListCreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [ForumPermission, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)


class ForumRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [ForumPermission, ]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return super().get_queryset().filter(forum_id=self.kwargs.get('forum_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            forum_id=self.kwargs.get('forum_id')
        )


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(forum_id=self.kwargs.get('forum_id'))

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user.author,
            forum_id=self.kwargs.get('forum_id')
        )
