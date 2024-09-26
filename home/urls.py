# urls.py
from django.urls import path
from .views import ExpenseListView, IncomeListView

urlpatterns = [
    #income views
    path("income/", IncomeListView.as_view(), name='incomeList'),

    #expense views
    path("expenses/", ExpenseListView.as_view(), name='expenseList'),
]