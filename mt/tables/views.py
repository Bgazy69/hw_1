from django.shortcuts import render, redirect
from .models import Table
from .forms import TableForm

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/table_list.html', {'tables': tables})

def table_create(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, 'tables/table_form.html', {'form': form})

def table_available(request):
    tables = Table.objects.filter(is_available=True)
    return render(request, 'tables/table_available.html', {'tables': tables})
