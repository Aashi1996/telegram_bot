import telebot
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from stats.models import Button, ButtonCall
from chat.models import Button

TELEGRAM_BOT_TOKEN = '<YOUR_TELEGRAM_BOT_TOKEN>'
YOUR_CHAT_ID = '<YOUR_CHAT_ID>'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@login_required
@csrf_exempt
def button_click(request, button_name):
    user = request.user
    button = Button.objects.get(name=button_name)

    button_call, _ = ButtonCall.objects.get_or_create(user=user, button=button)
    button_call.increment_count()

    joke = get_joke_by_button_name(button_name)

    # Increment button calls before sending the message
    button.increment_calls(user)

    bot.send_message(chat_id='<YOUR_CHAT_ID>', text=joke)
    return HttpResponse()

@csrf_exempt
def telegram_webhook(request):
    json_data = request.body.decode("utf-8")
    update = telebot.types.Update.de_json(json.loads(json_data))
    bot.process_new_updates([update])
    return HttpResponse()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    buttons = Button.objects.all()
    for button in buttons:
        markup.add(telebot.types.KeyboardButton(button.name))
    bot.send_message(chat_id=message.chat.id, text="Choose a button:", reply_markup=markup)

from django.http import JsonResponse

def get_joke_by_button_name(request, button_name):
    if button_name == 'stupid':
        joke = "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif button_name == 'fat':
        joke = "Why don't scientists trust atoms? Because they make up everything!"
    elif button_name == 'dumb':
        joke = "Why don't skeletons fight each other? They don't have the guts!"

    data = {
        'message': joke
    }

    return JsonResponse({'joke': joke})

@login_required
def chat_view(request):
    return render(request, 'chat.html')
