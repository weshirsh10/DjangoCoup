from django.contrib import admin
from .models import Card, Player
# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ('type', 'action', 'counteraction', 'state')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "coins", "card1", "card2", "state", 'turn')

admin.site.register(Card, CardAdmin)
admin.site.register(Player, PlayerAdmin)