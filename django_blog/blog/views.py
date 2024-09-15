from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm, CommentForm, PostForm
from .models import Post, Comment
from django.db.models import Q
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

# Create your views here.
def register(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login") 
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form":form})

@login_required
def profile(request):
    return render(request, "accounts/profile.html")


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    template_name = "post_confirm_delete.html"

@login_required
def CommentCreateView(request, post_pk):
    post = get_object_or_404(Post, post_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect("post_detail.html", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/comment_form.html", {"form":form})

@method_decorator(login_required, name="dispatch")
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "blog/comment_delete.html"

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    

@method_decorator(login_required, name="dispatch")
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)
    
    def get_success_url(self):
        return self.object.post.get_absolute_url()
    

def search_post(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query) |
            Q(tags__name__icontains = query)
        ).distinct

    else:
        posts = Post.objects.all()
    return render(request, "blog/search_results.html", {"posts":posts, "query":query})


class PostByTagListView(ListView):
    model = Post
    template_name = "blog/posts-by-tag.html"
    context_object_name = "post"

    def get_queryset(self):
        tag_slug = self.kwargs.get("tag_slug")
        return Post.objects.filter(tag_slug=tag_slug)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = self.kwargs.get("tag_slug")
        return context
