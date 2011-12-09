from django.http import HttpResponse

def login(request):
    html = "<html><body>Login page</body></html>"
    return HttpResponse(html)
    
def overview(request):
    html = "<html><body></body>Overview page</html>"    
    return HttpResponse(html)

def user(request, userid):
    html = "<html><body></body>User info for user %s</html>" % userid
    return HttpResponse(html)

