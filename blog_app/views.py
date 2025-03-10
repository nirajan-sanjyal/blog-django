from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog_app.models import Post
from django.utils import timezone
from django.shortcuts import redirect
from blog_app.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from blog_app.models import Post
from blog_app.forms import PostForm
from django.views.generic import ListView, UpdateView,CreateView,DeleteView, DetailView,View

def post_list(request):
    posts =Post.objects.filter(published_at__isnull = False).order_by("-published_at")
    return render (
        request,
        "post_list.html",
        {"posts": posts},
    )

def post_detail(request,pk):
    post =Post.objects.get(pk= pk, published_at__isnull = False)
    return render (
        request,
        "post_detail.html",
        {"post": post},
    )

@login_required
def draft_list(request):
    posts =Post.objects.filter( published_at__isnull = True)
    return render (
        request,
        "draft_list.html",
        {"posts": posts},
    )
@login_required
def draft_detail(request,pk):
    post =Post.objects.get(pk= pk, published_at__isnull = True)
    return render (
        request,
        "draft_detail.html",
        {"post": post},
    )



@login_required
def draft_publish(request, pk):
    post = Post.objects.get(pk= pk, published_at__isnull = True)
    post.published_at = timezone.now()
    post.save()
    return redirect("post_list")

@login_required
def post_create(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit= False)
            post.author= request.user
            post.save()
            return redirect("draft_detail", pk= post.pk)
    return render(
        request,
        "post_create.html",
        {"form": form},
    )

@login_required
def post_update(request ,pk):
    post = Post.objects.get(pk= pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            if post.published_at:
                return redirect("post_detail",post.pk)
            else:
                return redirect("draft_detail", post.pk)
            
    return render(
       request,
        "post_create.html",
        {"form": form}, 
    )
@login_required
def post_delete(request , pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect("post_list")

class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "darft_list.html"
    context_object_name= "posts"

    def get_queryset(self):
        return render(self.request, self.template_name)
