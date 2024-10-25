from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import ExpenceModel
from django.db.models import F
from django.db import transaction

def home(request):
    expense_lst = ExpenceModel.objects.all()
    return render(request,'home.html',{'expense_lst':expense_lst})

def add_expense(request):
    if request.method == 'POST':
        spender = request.POST.get('spender')
        amount = request.POST.get('amount')
        payment_mode = request.POST.get('payment_mode')
        payment_status = request.POST.get('payment_status')
        date = request.POST.get('date')
        
        ExpenceModel.objects.create(
            spender=spender,
            amount=amount,
            payment_mode=payment_mode,
            payment_status=payment_status,
            date=date
        )
        return redirect('home')
    return render(request, 'add_expense.html')

def update_expense(request, expense_sr):
    expense = get_object_or_404(ExpenceModel, sr=expense_sr)
    
    if request.method == 'POST':
        try:
            # Get the form data
            spender = request.POST.get('spender')
            amount = request.POST.get('amount')
            payment_mode = request.POST.get('payment_mode')
            payment_status = request.POST.get('payment_status')
            date = request.POST.get('date')
            
            # Update the expense object
            expense.spender = spender
            expense.amount = amount
            expense.payment_mode = payment_mode
            expense.payment_status = payment_status
            expense.date = date
            expense.save()
            
            # Add success message
            messages.success(request, 'Expense updated successfully!')
            return redirect('home')
            
        except Exception as e:
            # Add error message
            messages.error(request, f'Error updating expense: {str(e)}')
            return render(request, 'update_expense.html', {"expense": expense})
    
    return render(request, 'update_expense.html', {"expense": expense})

def delete_expense(request, expense_sr):
    # Perform the delete operation in a transaction
    with transaction.atomic():
        # Get and delete the expense
        expense = get_object_or_404(ExpenceModel, sr=expense_sr)
        deleted_sr = expense.sr
        expense.delete()
        
        # Update sr numbers for all expenses that came after the deleted one
        ExpenceModel.objects.filter(sr__gt=deleted_sr).update(sr=F('sr') - 1)
    
    return redirect('home')

# Create your views here.
