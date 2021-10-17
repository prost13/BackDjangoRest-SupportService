from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Assistant)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Ordering)
admin.site.register(Message)
admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(Authoring)

