from django.contrib import admin

from .models import Room, Topic, Message, User


class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'host', 'topic', 'updated', 'created')
    list_display_links = ('pk', 'name')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'room', 'user', 'updated', 'created')
    list_display_links = ('pk', 'room')


admin.site.register(User)
admin.site.register(Room, RoomAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Message, MessageAdmin)