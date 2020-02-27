from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    now = datetime.now()

    #html_content="<html><head><title>Hello, Django</title></head><body>"

    #html_content+="<strong>Hello Django!</strong></br>"
    #html_content+=now.strftime("%A, %d %B, %Y at %X")

    #html_content+="</body></html>"

    return render( 
        request, "HelloDjangoApp/index.html", {
            'title': "Hello Django",
            'content':'This is the current time on server: ',
            'current_time': now.strftime("%A, %d %B, %Y at %X"),
            }
        )

#def index(request):

    #return render(
    #    request,
    #    "HelloDjangoApp/index.html",  
    #    # Relative path from the 'templates' folder to the template file
    #    # "index.html", 
    #    # Use this code for VS 2017 15.7 and earlier
    #    {
    #        'content': "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #    }
    #)

#def index(request):
#    now = datetime.now()
#    html_body_code = now.strftime("%A, %d %B, %Y at %X")
#    return render(
#        request,
#        'HelloDjangoApp/index.html', context = {
#            'content': html_body_code,
#        }, content_type = "text/html", 
#    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )

