from django.contrib import admin
from support_back.models import Client, Assistant, Service, Order, Tag, Ordering, Message, Ticket, Review, Authoring

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

