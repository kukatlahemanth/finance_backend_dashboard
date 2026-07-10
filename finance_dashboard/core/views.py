from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import User, FinancialRecord
from .serializers import UserSerializer, FinancialRecordSerializer
from .permissions import IsAdmin, IsAnalyst
from django.db.models.functions import TruncMonth
from datetime import datetime
from .permissions import IsAdmin, IsAnalyst, IsViewer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

class FinancialRecordViewSet(ModelViewSet):
    serializer_class = FinancialRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'analyst']:
            queryset = FinancialRecord.objects.all()
        else:
            queryset = FinancialRecord.objects.none()
        type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        date = self.request.query_params.get('date')
        if type:
            queryset = queryset.filter(type=type)
        if category:
            queryset = queryset.filter(category=category)
        if date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
                queryset = queryset.filter(date=parsed_date)
            except ValueError:
                return queryset.none()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        elif self.action in ['list', 'retrieve']:
            return [IsAnalyst()]
        return [IsAuthenticated()]
    
class DashboardView(APIView):
    permission_classes = [IsViewer]
    def get(self, request):
        records = FinancialRecord.objects.all().order_by('-created_at')
        income = records.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expense = records.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        category_summary = records.values('category').annotate(total=Sum('amount'))
        recent_activity = records[:5].values(
            'amount', 'type', 'category', 'date')
        monthly_trends = records.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')

        return Response({
            "total_income": income,
            "total_expense": expense,
            "net_balance": income - expense,
            "category_summary": list(category_summary),
            "recent_activity": list(recent_activity),
            "monthly_trends": list(monthly_trends)})