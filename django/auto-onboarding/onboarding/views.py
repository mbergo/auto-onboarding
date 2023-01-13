from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        subprocess.run(["python", "create_user.py", name, email, password])
        return HttpResponse("User created!")
    else:
        return render(request, 'create_user.html')

