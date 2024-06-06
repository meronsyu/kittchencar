from django.urls import include, path
from rest_framework import routers
from .views import MemoViewSet

router = routers.DefaultRouter()
router.register('memos', MemoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]