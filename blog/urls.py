
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers 
from . import views

router = routers.SimpleRouter()
router.register(r'articles',views.ArticleViewSet)
router.register(r'comments',views.CommentViewSet)
router.register(r'tags',views.TagViewSet)
router.register(r'categories',views.CategoryViewSet)

router.register(r'users',views.UserViewSet)
urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/token/',views.DecoratedTokenObtainPairView.as_view(),name="token"),
    path('api/token/refresh/',views.DecoratedTokenRefreshView.as_view(),name="refresh_token"),
]

urlpatterns+=router.urls