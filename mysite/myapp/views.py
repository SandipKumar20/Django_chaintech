from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserSubmission
from django.contrib import messages
from datetime import datetime
import pyquotegen

# Create your views here.
# A function to display the home page.
def home(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    quote = pyquotegen.get_quote()
    return render(request, 'myapp/index.html', {'current_time': current_time, 'quote': quote})

# A function to display the form
def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        submission = UserSubmission(name=name, email=email)
        submission.save()
        messages.success(request, f'Thank you {name}, we have received your email: {email}')
        return redirect('home')
    return HttpResponse('Invalid request.')

# A function to display all the submissions
def submissions(request):
    submissions = UserSubmission.objects.all()
    return render(request, 'myapp/submissions.html', {'submissions': submissions})