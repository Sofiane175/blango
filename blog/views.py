from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.user.is_active:  # ✅ Properly indented
        if request.method == "POST":  # ✅ Nested under is_active
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:  # ✅ Aligned with if request.method == "POST"
            comment_form = CommentForm()
    else:  # ✅ Correct else for is_active check
        comment_form = None

    return render(  # ✅ Properly aligned
        request, 
        "blog/post-detail.html", 
        {"post": post, "comment_form": comment_form}
    )