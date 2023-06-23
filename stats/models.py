from django.db import models
from django.contrib.auth.models import User
from chat.models import Button

class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    button_calls = models.ManyToManyField(Button, through='ButtonCall')

    def __str__(self):
        return self.user.username

    def get_total_calls(self):
        return self.buttons.aggregate(total_calls=models.Sum('buttoncall__count')).get('total_calls', 0)

class ButtonCall(models.Model):
    button = models.ForeignKey(Button, on_delete=models.CASCADE)
    user_stats = models.ForeignKey(UserStats, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.button} - {self.user_stats} - {self.count}"
