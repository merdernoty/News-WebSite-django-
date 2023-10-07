from django.shortcuts import render


def index(request):
    data = {
        "title": "Main Page",
        "values": ["Some", "Hi","Dog"],
        "obj": {
            "car":"porshe",
            "age":17,
            "hobby": "Football"

        }
    }
    return render(request,"main/index.html", data)

def about(request):
    return render(request,"main/about.html")