from django.shortcuts import render
import random

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
        
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = util.get_entry(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
               "title": entry_search,
               "content": html_content
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists."
            })
        else:
            util.save_entry(title, content)
            html_content = util.get_entry(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })

def edit(request):   
    if request.method == 'POST':
        title = request.POST['entry_title']
        content = util.get_entry(title)      
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
        
def save_edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = util.get_entry(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
            })
        
def rand(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = util.get_entry(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title" : rand_entry,
        "content" : html_content  
    })