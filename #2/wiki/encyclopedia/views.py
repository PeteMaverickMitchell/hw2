from django.shortcuts import render

from . import util
        
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    html_content = util.get_entry(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message" : "This entry does not exist."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })