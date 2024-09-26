from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from .models import Income, Expense
# Create your views here.

class ExpenseListView(ListView):
    model = Expense

class ExpenseDetailView(DetailView):
    model = Expense

class ExpenseUpdateView(UpdateView):
    model = Expense

class ExpenseDeleteView(DeleteView):
    model = Expense

#################################################################################
class IncomeListView(ListView):
    model = Income

class IncomeDetailView(DetailView):
    model =  Income

class IncomeUpdateView(UpdateView):
    model =  Income

class IncomeDeleteView(DeleteView):
    model =  Income


