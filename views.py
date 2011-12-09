from django.http import HttpResponse

def login(request):
    html = "<html><body>Login page</body></html>"
    return HttpResponse(html)
    
def overview(request):
    html = "<html><body></body>Overview page</html>"    
    return HttpResponse(html)

def user(request, userid):
    if userid == '':
        html = "<html><body></body>Your account information </html>"
    else:
        html = "<html><body></body>User information for user %s</html>" % userid
    return HttpResponse(html)
    
def route(request, routeid):
    if userid == '':
        html = "<html><body></body>You must specify a route</html>"
    elif routeid == 'new':
        html = "<html><body></body>Create a new route</html>"
    else:
        html = "<html><body></body>Information for route %s</html>" % userid
    return HttpResponse(html)

def user_routes(request, userid):
    if userid == '':
        html = "<html><body></body>Routes you are currently participating in</html>"
    else:
        html = "<html><body></body>Routes user %s currently participates in</html>" % userid
    return HttpResponse(html)

def user_routes_history(request, userid):
    if userid == '':
        html = "<html><body></body>Your routes history</html>"
    else:
        html = "<html><body></body>Routes history for user %s</html>" % userid
    return HttpResponse(html)
    


