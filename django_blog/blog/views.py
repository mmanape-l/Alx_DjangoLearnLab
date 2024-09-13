from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import UserUpdateForm, PostForm, CommentForm

# Profile view for user profile updates
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})

# ListView for displaying all posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # Custom template for listing posts
    context_object_name = 'posts'  # Name of the context object to use in the template
    ordering = ['-published_date']  # Display posts in descending order of published date

# DetailView for displaying a single post along with comments
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # Custom template for viewing a single post
    context_object_name = 'post'  # Name of the context object to use in the template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the comment form to the context
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
        return context

# CreateView for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use PostForm to handle post creation
    template_name = 'post_form.html'  # Custom form template
    success_url = reverse_lazy('post-list')  # Redirect after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author to the logged-in user
        return super().form_valid(form)

# UpdateView for editing an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use PostForm to handle post updates
    template_name = 'post_form.html'  # Reuse the same form template as for creation
    success_url = reverse_lazy('post-list')  # Redirect after successful update

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can edit the post

# DeleteView for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'  # Template for confirmation before deletion
    success_url = reverse_lazy('post-list')  # Redirect after successful deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only the author can delete the post

# View for adding a new comment
@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm()
    return redirect('post-detail', pk=post_id)

# View for updating an existing comment
@login_required
def update_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'form': form})

# View for deleting a comment
@login_required
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post_id=post_id, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('post-detail', pk=post_id)
    return render(request, 'comment_confirm_delete.html', {'comment': comment})
