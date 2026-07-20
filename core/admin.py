from django.contrib import admin
from .models import Client, Video, Signal, Alert

admin.site.register(Client)
admin.site.register(Video)
admin.site.register(Signal)
admin.site.register(Alert)