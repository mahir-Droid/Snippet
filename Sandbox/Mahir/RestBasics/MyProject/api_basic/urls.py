from django.urls import path, include
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, article_list, article_detail, ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
   # path('article/', article_list),
   # path('detail/<int:pk>/', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))
]
