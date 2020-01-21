from django.shortcuts import (
    render,
    redirect,
)

from .models import Issue
from .forms import IssueForm
from .tasks import create_new_issue


def index(request):
    return render(
        request,
        'tasks/index.html',
        {'tasks': Issue.objects.all()}
    )


def new(request):
    if request.method == 'GET':
        return render(
            request,
            'tasks/new.html',
            {'form': IssueForm()}
        )
    elif request.method == 'POST':
        if request.POST['name']:
            create_new_issue.delay(request.POST['name'])
            return redirect('/tasks/')
        else:
            return redirect('/tasks/new/')
