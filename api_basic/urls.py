
from django.urls import path, include 
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet, GenericAPIViewSet,ArticleModleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

router2 = DefaultRouter()
router2.register('article', GenericAPIViewSet, basename='article')

ArticleModleViewSet
router3 = DefaultRouter()
router3.register('article', ArticleModleViewSet, basename='article')

urlpatterns = [

    path('modelviewset/', include(router3.urls)),
    path('modelviewset/<int:pk>', include(router3.urls)),

    path('genericviewset/', include(router2.urls)),
    path('genericviewset/<int:pk>', include(router2.urls)),

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

#    path('article/', article_list), 
    path('article/', ArticleAPIView.as_view()), 
#    path('detail/<int:pk>/', article_detail)
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()), 
]