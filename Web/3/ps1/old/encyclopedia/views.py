from django.shortcuts import render
from django.http import Http404
import markdown2
from . import util


def index(request):
    entries = util.list_entries()
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def wiki(request, item):
    entries = util.list_entries()
    ENTRIES = [entry.upper() for entry in entries]
    
    print(item.upper())
    print(ENTRIES)
    
    if item.upper() in ENTRIES:
        content = markdown2.markdown(util.get_entry(item))
        return render(request, "encyclopedia/entry.html", {
            "header": item,
            "content": content,
        })
    else: 
        return render(request, "encyclopedia/page404.html")

