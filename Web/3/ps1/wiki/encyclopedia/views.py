from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    entries = util.list_entries()
    ENTRIES = [entry.upper() for entry in entries]
    if title.upper() in ENTRIES:
        content = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "exists": False
        })
    
def search(request):
    query = request.GET.get('q') 
    entries = util.list_entries()
    ENTRIES = [entry.upper() for entry in entries]
    if query.upper() in ENTRIES:
        content = markdown2.markdown(util.get_entry(query))
        return render(request, "encyclopedia/page.html", {
            "title": query,
            "content": content
        })
    else: 
        results = []    
        for entry in entries:
            if query.upper() in entry.upper(): 
                results.append(entry)
        
        if len(results) == 0:
            return render(request, "encyclopedia/error.html", {
                "title": query,
                "exists": False
            })
        else:
            return render(request, "encyclopedia/search.html", {
                "query": query,
                "results": results
            })

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        entries = util.list_entries()
        ENTRIES = [entry.upper() for entry in entries]
        if title.upper() in ENTRIES:
            return render(request, "encyclopedia/error.html", {
                "title": title,
                "exists": True
            })
        else:
            util.save_entry(title, content)
            content = markdown2.markdown(util.get_entry(title))
            return render(request, "encyclopedia/page.html", {
                "title": title,
                "content": content
            })
    return render(request, "encyclopedia/create.html")  

def edit(request, title):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        content = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": content
        })
    else:
        # title = request.GET.get('title')
        content = markdown2.markdown(util.get_entry(title))
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

def test(request):
    return HttpResponse("Hello, world. You're at the polls index.")