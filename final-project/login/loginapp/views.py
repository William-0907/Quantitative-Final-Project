from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,get_user_model 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Scores

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('users')
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, "You have successfully logged in.")
            return redirect('users')
        else:
            messages.warning(request, "Invalid Username or Password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'loginapp/login.html')

@login_required
def users_view(request):
    User = get_user_model()
    all_users = User.objects.all()
    return render(request,'loginapp/users.html', {'all_users':all_users})

@login_required
def stats_view(request):
    User = get_user_model()
    total_users = User.objects.count()
    return render(request,'loginapp/user_stats.html', {'total_users':total_users})

@login_required
def graph_view(request):
    scores = Scores.objects.all()
    score_data = [score.score for score in scores]
    users = [score.user.username for score in scores]
    return render(request,'loginapp/graphs.html', {'score_data':score_data, 'users':users})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
