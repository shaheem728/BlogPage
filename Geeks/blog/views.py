from django.shortcuts import render,HttpResponse,redirect, get_object_or_404
from django.contrib import messages
from .models import Post, BlogComment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.
def blogPage(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,"blog/blogPage.html",context)
def blogPost(request, Sno):
    post = get_object_or_404(Post, Sno=Sno)
    comments = BlogComment.objects.filter(post=post)
    context = {
        'post': post,  # Ensure 'post' is included in the context
        'comments': comments,
        'user': request.user
    }
    return render(request, "blog/blogPost.html", context)

@login_required
def add_comment(request):
    if request.method == "POST":
        comment_text = request.POST.get('posting')  # Comment text
        post_id = request.POST.get('postSno', None)  # Use 'postSno' for the primary key
        parent_id = request.POST.get('parentSno', None)  # Use 'parentSno' for the parent comment

        if not comment_text:
            return JsonResponse({"error": "Comment cannot be empty"}, status=400)

        # Use 'Sno' instead of 'id' to fetch the Post
        post = get_object_or_404(Post, Sno=post_id)
        parent = None

        if parent_id:
            parent = get_object_or_404(BlogComment, sno=parent_id)

        # Create and save the comment
        comment = BlogComment(
            comment=comment_text,
            user=request.user,
            post=post,
            parent=parent
        )
        comment.save()

    return redirect('list_comments', post_id=comment.post.Sno)



   

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(BlogComment, sno=comment_id, user=request.user)
    comment.delete()
    return redirect('list_comments', post_id=comment.post.Sno)


def list_comments(request, post_id):
    # Use 'Sno' as it's the primary key in the Post model
    post = get_object_or_404(Post, Sno=post_id)
    comments = BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp')
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)

    context = {
        'post': post,
        'comments': comments,
        'replies': replies,
    }
    return render(request, 'blog/post_list.html', context)

    