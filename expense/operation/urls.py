from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('update_expense/<int:expense_sr>/', views.update_expense, name='update_expense'),
    path('delete_expense/<int:expense_sr>/', views.delete_expense, name='delete_expense'),
]