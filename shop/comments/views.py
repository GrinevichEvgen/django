from django.shortcuts import render, redirect

from comments.forms import AddCommentForm
from comments.models import Comment


# Create your views here.

def comments(request):
    Comment.objects.all()
    return render(request, "comments.html", {"comments": comments})


def add_comments(request):
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(title=form.cleaned_data["title"], text=form.cleaned_data["content"],
                                author=request.user)

            return redirect("/comments/")
    else:
        form = AddCommentForm()
    return render(request, "add_note.html", {"form": form})