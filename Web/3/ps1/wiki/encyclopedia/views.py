from django.shortcuts import render
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
            "title": title
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
        for entry in entries:
            if query.upper() == entry.upper():
                content = markdown2.markdown(util.get_entry(entry))
                return render(request, "encyclopedia/page.html", {
                    "title": entry,
                    "content": content
                })
        results = []
        for entry in entries:
            if query.upper() in entry.upper():
                results.append(entry)
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": results
        })