from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Member
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('admin:index')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='admin:login')
def all_members(request):
    member_list = Member.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(member_list, 10)

    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    
    context = {
        'members': members
    }
    return render(request, 'main/all_members.html', context)