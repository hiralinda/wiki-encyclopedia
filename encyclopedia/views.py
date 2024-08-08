from django.shortcuts import render, redirect
from . import util
import markdown, random
from django.conf import settings
import os

def random_page(request):
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect('entry_page', title=random_entry)
    return render(request, "encyclopedia/error.html", {
        "message": "No entries available."
    })

def delete_page(request, title):
    if request.method == "POST":
        # Ensure you have a proper function to delete the entry
        filename = f"entries/{title}.md"
        filepath = os.path.join(settings.BASE_DIR, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            return redirect('index')
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "The requested page does not exist."
            })
    return render(request, "encyclopedia/error.html", {
        "message": "Invalid request method."
    })

def edit_page(request, title):
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect('entry_page', title=title)

    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })

    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": content
    })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        if util.get_entry(title):
            return render(request, "encyclopedia/new_page.html", {
                "error": "An entry with this title already exists.",
                "title": title,
                "content": content
            })

        util.save_entry(title, content)
        return redirect('entry_page', title=title)

    return render(request, "encyclopedia/new_page.html")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert_html(title):
    text = util.get_entry(title)
    md = markdown.Markdown()
    if text == None:
        return None
    else:
        return md.convert(text)

    
def entry_page(request, title):
    content = convert_html(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    query = request.GET.get('q', '')
    if query:
        entry = util.get_entry(query)
        if entry:
            return redirect('entry_page', title=query)
        else:
            entries = util.list_entries()
            matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
            return render(request, "encyclopedia/search_results.html", {
                "query": query,
                "entries": matching_entries
            })
    return redirect('index')