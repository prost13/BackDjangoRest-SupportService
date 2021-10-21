from django.db import models
from django.contrib.auth.models import User
from support_back.choices import Choices

class Assistant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return 'User: {}, phone: {}'.format(self.user, self.phone)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return 'User: {}, phone: {}'.format(self.user, self.phone)

class Service(models.Model):
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=100)
    service_type = models.CharField(choices=Choices.SERVICE_TYPES, default='1', max_length=1)

    def __str__(self):
        return '{}, {}'.format(self.name, self.get_service_type_display())

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=100)
    order_type = models.CharField(choices=Choices.ORDER_TYPES, default='1', max_length=1)

    def __str__(self):
        return '{}, {}'.format(self.name, self.get_order_type_display())

class Tag(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)

class Ordering(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    deadline = models.DateTimeField()

    def __str__(self):
        return '{} - {}, Client: {}, Assistant: {}'.format(self.order_date, self.deadline, self.client, self.assistant)

class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE)
    msg_date = models.DateTimeField()
    is_edited = models.BooleanField(default=False)
    desc = models.CharField(max_length=1000)

class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, blank=True, null=True)
    severity = models.CharField(choices=Choices.SEVERITIES, default='1', max_length=1)
    desc = models.CharField(max_length=1000)
    ticket_date = models.DateTimeField()
    is_resolved = models.BooleanField(default=True)

    def __str__(self):
        return '{}, {}, Is Resolved? {}'.format(self.get_severity_display(), self.ticket_date, self.is_resolved)

class Review(models.Model):
    rating = models.CharField(choices=Choices.RATTING_FILLED, default='1', max_length=1)
    desc = models.CharField(max_length=1000)

class Authoring(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateTimeField()

    def __str__(self):
        return '{}, {}'.format(self.author, self.review_date)




