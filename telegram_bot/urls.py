"""
URL configuration for telegram_bot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from chat.views import button_click, telegram_webhook, chat_view, get_joke_by_button_name
from stats.views import user_stats

urlpatterns = [
    path('button/<str:button_name>/', button_click, name='button_click'),
    path('telegram_webhook/', telegram_webhook, name='telegram_webhook'),
    path('chat/', chat_view, name='chat'),
    path('user_stats/', user_stats, name='user_stats'),
    path('get_joke/<str:button_name>/', get_joke_by_button_name, name='get_joke_by_button_name'),
]
