from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

def news_home(request):
    data = {
        "title":"News on Our Website",
        # "news":Article.objects.all()
        "news":Article.objects.order_by("-date")#[:0]
    }
    return render(request, "news/news_home.html", data )

def create(request):
    error = ""
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:  
            error = "Form is not valid"

    form = ArticleForm()

    data = {
        "title":"Create new News",
        "error": error,
        "form": ArticleForm()
    }

    return render(request, "news/create.html", data )

    