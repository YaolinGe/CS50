from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request):
    return render(request, "encyclopedia/wiki.html", {
        "entries": util.list_entries()
    })

def css(request):
    if util.get_entry("CSS"):
        text = markdown2.markdown(util.get_entry("CSS"))
        is_header = text.find("<h1>")
        ie_header = text.find("</h1>")
        header = text[is_header+4:ie_header]
        is_content = text.find("<p>")
        ie_content = text.find("</p>")
        content = text[is_content+3:ie_content]
    
        return render(request, "encyclopedia/entry.html", {
            "header": header,
            "content": content,
        })
    else:
        pass

# def entry(request, title):
#     return render(request, "encyclopedia/entry.html", {
#         "entry": util.get_entry(title)
#     })
