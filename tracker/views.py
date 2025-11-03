
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from datetime import date

def home(request):
    expenses = Expense.objects.all().order_by('-date')
    total = sum(exp.amount for exp in expenses)
    return render(request, 'home.html', {'expenses': expenses, 'total': total})

def add_expense(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        amount = request.POST['amount']
        exp_date = request.POST['date']
        note = request.POST.get('note', '')
        Expense.objects.create(title=title, category=category, amount=amount, date=exp_date, note=note)
        return redirect('home')
    return render(request, 'add_expense.html')

def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.title = request.POST['title']
        expense.category = request.POST['category']
        expense.amount = request.POST['amount']
        expense.date = request.POST['date']
        expense.note = request.POST.get('note', '')
        expense.save()
        return redirect('home')
    return render(request, 'edit_expense.html', {'expense': expense})

def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('home')


# Create your views here.
