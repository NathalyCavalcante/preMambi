from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from worker.models import Member

# Create your views here.
@login_required
def index(request):
    member = Member.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'member': member
    })


