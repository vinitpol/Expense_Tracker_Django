from django.contrib import admin
from .models import ExpenceModel

# Register your models here.

@admin.register(ExpenceModel)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['spender', 'amount', 'payment_mode', 'payment_status', 'date']

