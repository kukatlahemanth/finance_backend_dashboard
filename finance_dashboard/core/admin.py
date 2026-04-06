from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, FinancialRecord

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'role', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(FinancialRecord)









































































