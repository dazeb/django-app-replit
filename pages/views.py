from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello There</h1>") # String of HTML Code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>") # String of HTML Code
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1>About Page</h1>") # String of HTML Code
    my_context = {
      "my_text": "This is about us",
      "my_number": 123,
      "my_list": [123, 3456, 4567]
    }
    return render(request, "about.html", my_context)