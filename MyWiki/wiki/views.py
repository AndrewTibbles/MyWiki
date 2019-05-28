from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.db.models import F

from .forms import UploadFileForm
from .models import Page, SignUpForm, UserFileUpload

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
        page.counter = F('counter') + 1
        page.save(update_fields=['counter'])
        page.refresh_from_db()
        return render(request, 'wiki/detail.html', {'page': page})

    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk})

@login_required
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

@login_required
def save_page(request, pk):
    content = request.POST['content']
    try:
        page = Page.objects.get(pk=pk)
        page.content = content
    except Page.DoesNotExist:
        page = Page(title=pk, content=content)
    if 'Save' in request.POST:
        page.save()
    return redirect(page)

@login_required
def delete_page(request, pk):
    try:
        Page.objects.get(pk=pk)
        return render(request, "wiki/delete_page.html",
        {
            'page_name': pk
        })
    except Page.DoesNotExist:
        return redirect('wiki:index')

@login_required
def delete_confirm(request, pk):
    page = Page.objects.get(pk=pk)
    if 'Delete' in request.POST:
        page.delete()
    return redirect('wiki:index')

def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('wiki:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)

def test_500_error(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)

def test_404_error(request):
    # Return an "Internal Server Error" 404 response code.
    return HttpResponse(status=404)

def test_407_error(request):
    # Return an "Internal Server Error" 407 response code.
    return HttpResponse(status=407)

#import logging

#from django.http import HttpResponse

# This retrieves a Python logging instance (or creates it)
#logger = logging.getLogger(__name__)

#def index(request):
    # Send the Test!! log message to standard out
 #   logger.error("Test!!")
 #   return HttpResponse("Hello logging world.")