from django.shortcuts import render
from rest_framework import viewsets
from . serializers import (
    CategorySerializer,
    ArticleSerializer,
    TagSerializer,
    CommentSerializer,
    UserSerialzier,
    TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer
    )
from . models  import ArticleUser,Articles,Category,Comments,Tag
from drf_spectacular.utils import extend_schema
from rest_framework import permissions,status,parsers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend



class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerialzier
    queryset = ArticleUser.objects.all()
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    throttle_scope = 'users'
   

    @extend_schema(tags=['Auth'],summary='create new  user',description='signup to get your access token to make request')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='get by  user id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='list all  user')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='partical update  user')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='update  user')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Auth'],summary='delete user')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.FormParser,parsers.MultiPartParser]
    throttle_scope = 'articles'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['headlines']
    search_fields = ['=headlines']

    @extend_schema(tags=['Content'],summary='create new articles')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Content'],summary='get by articles id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Content'],summary='list all articles')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Content'],summary='partical update articles')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Content'],summary='update articles')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Content'],summary='delete articles')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'categories'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['=name']

    @extend_schema(tags=['Category'],summary='create new category')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='get by category id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='list all category')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='partical update category')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='update category')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Category'],summary='delete category')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'comments'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['content']
    search_fields = ['=content']

    @extend_schema(tags=['Comment'],summary='create new comment')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Comment'],summary='get by comment id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Comment'],summary='list all comment')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Comment'],summary='partical update comment')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Comment'],summary='update comment')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Comment'],summary='delete comment')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'tags'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['=name']

    @extend_schema(tags=['Tag'],summary='create new  tag',description='create new tag')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=['Tag'],summary='get by  tag id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=['Tag'],summary='list all  tag')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=['Tag'],summary='partical update  tag')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=['Tag'],summary='update  tag')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=['Tag'],summary='delete tag')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    

    
class DecoratedTokenObtainPairView(TokenObtainPairView):
    @extend_schema(tags=['Auth'],summary='get token',
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class DecoratedTokenRefreshView(TokenRefreshView):
    @extend_schema(tags=['Auth'],summary='refresh token',
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)