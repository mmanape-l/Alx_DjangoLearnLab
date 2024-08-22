from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('yourapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('yourapp.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'book_form.html')

@permission_required('yourapp.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'book_form.html', {'book': book})

@permission_required('yourapp.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})
