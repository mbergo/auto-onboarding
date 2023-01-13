from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        subprocess.run(["python", "create_user.py", name, email, password])
        return HttpResponse("User created!")
    else:
        return render(request, 'create_user.html')

