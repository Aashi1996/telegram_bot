from django.shortcuts import render
from .models import UserStats

def user_stats(request):
    user_stats = UserStats.objects.all()
    return render(request, 'stats/user_stats.html', {'user_stats': user_stats})
