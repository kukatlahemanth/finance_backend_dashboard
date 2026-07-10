from rest_framework import serializers
from .models import User, FinancialRecord

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role', 'is_active','last_login']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class FinancialRecordSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = FinancialRecord
        fields = ['id', 'amount', 'type', 'category', 'date', 'note', 'user']
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value

    def validate_category(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category cannot be empty")
        return value

    def validate(self, data):
        if data['type'] not in ['income', 'expense']:
            raise serializers.ValidationError("Type must be 'income' or 'expense'")
        return data