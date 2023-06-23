from django.db import models
from django.contrib.auth.models import User

class Button(models.Model):
    name = models.CharField(max_length=255)
    calls = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def increment_calls(self, user):
        self.calls += 1
        self.save()
        user_stats, _ = UserStats.objects.get_or_create(user=user)
        button_call, _ = ButtonCall.objects.get_or_create(button=self, user_stats=user_stats)
        button_call.count += 1
        button_call.save()
