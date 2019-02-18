from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects
    # print('jobs', jobs.summary)
    return render(request, 'jobs/home.html', {'jobs': jobs})
