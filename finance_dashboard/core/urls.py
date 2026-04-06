from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FinancialRecordViewSet, DashboardView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('records', FinancialRecordViewSet, basename='records')
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', DashboardView.as_view()),
]