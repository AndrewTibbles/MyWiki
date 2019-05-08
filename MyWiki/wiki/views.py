from django.views import generic
from django.shortcuts import render, redirect
from .models import Page


class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter()


class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'

    def get_queryset(self):
        return Page.objects.filter()


def View_Page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        return render(request, 'wiki/detail.html', {'page': page})

    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk})


def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content = ""

    return render(request, 'wiki/edit_page.html', 
    {
        'page_name': pk,
        'content': content
    })

def save_page(request, pk):
    if 'Save' in request.POST:
        content = request.POST['content']
        try:
            page = Page.objects.get(pk=pk)
            page.content = content
        except Page.DoesNotExist:
            page = Page(title=pk, content=content)
        page.save()
    return redirect('wiki:detail', pk=pk)