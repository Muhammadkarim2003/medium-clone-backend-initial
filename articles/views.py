from rest_framework import viewsets, permissions
from .models import Article
from .serializers import ArticleCreateSerializer, ArticleDetailSerializer

class ArticlesView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreateSerializer
        return ArticleDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
