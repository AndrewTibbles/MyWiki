from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.db.models import F

from .forms import UploadFileForm
from .models import Page, SignUpForm, UserFileUpload

# Sets the view for the index page.
class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.filter()

# Previous method of viewing pages now updated in View_Page
#class DetailView(generic.DetailView):
#    model = Page
#    template_name = 'wiki/detail.html'

#    def get_queryset(self):
#        return Page.objects.filter()

def View_Page(request, pk):
    try:
        page = Page.objects.get(pk=pk) # Gets the pages primary key - title
        page.counter = F('counter') + 1 # adds 1 to the pages counter
        page.save(update_fields=['counter']) # saves this value to the database
        page.refresh_from_db() # Refreshes the value from the database
        return render(request, 'wiki/detail.html', {'page': page}) # Renders the desired page.

    except Page.DoesNotExist:
        return render(request, 'wiki/create_page.html', {'page_name': pk}) # Navigate to page creation if it doesnt exist.

@login_required
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk) # Gets the pages title
        content = page.content # Gets the pages content
    except Page.DoesNotExist: # if the page doesn't exist default the content to an empty string
        content = ""

    return render(request, 'wiki/edit_page.html', # Render the edit page
    {
        'page_name': pk,
        'content': content
    })

@login_required
def save_page(request, pk):
    content = request.POST['content']
    try:
        page = Page.objects.get(pk=pk) # Gets the pages title
        page.content = content # Gets the pages content
    except Page.DoesNotExist:  # if the page doesn't exist create it.
        page = Page(title=pk, content=content)
    if 'Save' in request.POST: # if gets post `Save` then save the pages content and update the database
        page.save()
    return redirect(page) # redirect to the page

@login_required
def delete_page(request, pk):
    try:
        Page.objects.get(pk=pk) # Gets the pages title
        return render(request, "wiki/delete_page.html", # renders the page deletion confirmation page
        {
            'page_name': pk
        })
    except Page.DoesNotExist: # if the page doesnt exist return to the index page
        return redirect('wiki:index')

@login_required
def delete_confirm(request, pk):
    page = Page.objects.get(pk=pk)  # Gets the pages title
    if 'Delete' in request.POST:
        page.delete() # if gets post `delete` then delete the page and remove it from the database
    return redirect('wiki:index') # redirect the user to the index page.

def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) # gets the Signupform from models.py
        if form.is_valid(): # checks if the form is valid
            form.save() # save it to the database
            username = form.cleaned_data.get('username') # use the signup credentials
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user) #s signin to the newly created page
            return redirect('wiki:index') #render the index page as is_authenicated
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# adds the ability to upload files to the page
@login_required
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid(): # checks if the form is valid before saving it
            form.save() # save the form
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload') # display the files on the page ordered by upload order
    return render(request, 'wiki/upload.html', context) # renderes the upload page with the uploaded files

def test_500_error(request):
    # Return an "Internal Server Error" 500 response code.
    return HttpResponse(status=500)

def test_404_error(request):
    # Return an "Internal Server Error" 404 response code.
    return HttpResponse(status=404)

def test_407_error(request):
    # Return an "Internal Server Error" 407 response code.
    return HttpResponse(status=407)