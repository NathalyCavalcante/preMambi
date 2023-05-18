from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from worker.models import Member, Professions

# Create your views here.
@login_required
def index(request):
    member = Member.objects.filter(created_by=request.user)
    professions = Professions.objects.all()

    return render(request, 'dashboard/index.html', {
        'member': member,
        'professions': professions,

    })


