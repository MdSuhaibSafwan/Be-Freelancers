from django.shortcuts import render
from django.contrib.auth import get_user_model


User = get_user_model()

def index(request):
    user = request.user
    if user.is_authenticated:
        print("Redirecting to Work Page")
        pass

    
    context = {

    }
    return render(request, "main/index.html", context)
