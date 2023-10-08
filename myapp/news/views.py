from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    data = {
        "title":"News on Our Website",
        # "news":Article.objects.all()
        "news":Article.objects.order_by("-date")#[:0]
    }
    return render(request, "news/news_home.html", data )


class NewsDetailView(DetailView):
    model = Article 
    template_name= "news/detail_view.html"
    context_object_name = "article"

class NewsUpdateView(UpdateView):
    model = Article 
    template_name= "news/create.html"
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = "/news/"
    template_name = "news/newsdelete.html"

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

    