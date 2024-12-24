from django.http import HttpResponse

def set_session(request):
    # Set a session variable
    request.session['user_name'] = 'John Doe'
    return HttpResponse("Session data set")

def get_session(request):
    # Get a session variable
    user_name = request.session.get('user_name', 'Guest')
    return HttpResponse(f"Hello, {user_name}")

def set_cookie(request):
    response = HttpResponse("Cookie has been set")
    response.set_cookie('user_name', 'John Doe', max_age=3600)  # Expires in 1 hour
    return response
def get_cookie(request):
    user_name = request.COOKIES.get('user_name', 'Guest')
    return HttpResponse(f"Hello, {user_name}")
def delete_cookie(request):
    response = HttpResponse("Cookie has been deleted")
    response.delete_cookie('user_name')
    return response

def delete_session(request):
    # Clear the session data and delete the session ID cookie
    request.session.flush()
    return HttpResponse("Session has been deleted and user logged out.")


