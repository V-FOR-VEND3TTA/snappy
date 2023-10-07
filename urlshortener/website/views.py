from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# the view we get when we click the link
def create(request):
    if request.method == 'POST':
        url = request.POST['link'] # take the URL given to you by the user
        uid = str(uuid.uuid4())[:5] # give the URL an id that will be a maximum of 6 characters
        new_url = Url(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
