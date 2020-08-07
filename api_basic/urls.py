#Api basics/Url
from django.urls import path,include
from .views import article_lis,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='articlez')

urlpatterns = [
    #path('articles/', article_lis),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('articles/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>', article_detail),
    path('detail/<int:id>', ArticleDetails.as_view()),
    path('generic/<int:id>', GenericAPIView.as_view()),
    path('generic/', GenericAPIView.as_view())
    ]