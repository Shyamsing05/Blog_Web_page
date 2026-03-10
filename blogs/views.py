from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse
from django.conf import settings
from datetime import date
from .models import Post
from .forms import CommentForm




def home_page(request):
    latest_blogs = Post.objects.all().order_by("-date") [:2]
    return render(request, "blogs/index.html",{"l_blogs":latest_blogs})


def blogposts(request):
    blog_details = Post.objects.all()
    return render(request, "all-posts.html", {"blogs":blog_details})

def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list)
    return render(request, "blogs/process_blog_name.html")

def blog_post(request, blog):
    try:
          post_data = Post.objects.get(slug=blog)
          tag_caption = post_data.tags.all()
          form_data = CommentForm()
          return render(request, "blogs/posts.html", {"post": post_data, "tags": tag_caption, "comment_form": form_data})
    except Exception:
            return HttpResponseNotFound("<h1>blog not found</h1>")



