from django.contrib import admin
from .models import Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']
    list_display = ['__str__', 'user']

    class Meta:
        model = Tweet
