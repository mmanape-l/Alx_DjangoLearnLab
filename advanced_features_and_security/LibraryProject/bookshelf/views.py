from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from django.db import transaction
from django.core.exceptions import PermissionDenied
from django.utils.html import escape
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
@require_http_methods(["GET"])
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
@require_http_methods(["GET", "POST"])
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        with transaction.atomic():
            book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

@require_http_methods(["GET", "POST"])
def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data
            # Escape user input if it's going to be displayed
            safe_data = {k: escape(v) for k, v in form.cleaned_data.items()}
            # Use safe_data for further processing
            return redirect('some_success_url')
    else:
        form = ExampleForm()
    return render(request, 'example_form.html', {'form': form})