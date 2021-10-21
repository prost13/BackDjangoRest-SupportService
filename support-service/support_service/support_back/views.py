from rest_framework import generics, permissions, viewsets, filters
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from support_back.permissions import IsAssistant
from django_filters.rest_framework import DjangoFilterBackend

from support_back.models import Client, Assistant, Service, Order, Tag, Ordering, Message, Ticket, Review, Authoring
from support_back.serializers import UserSerializer, AssistantSerializer, CreateAssistantSerializer, \
    ClientSerializer,  CreateClientSerializer, ServiceSerializer, CreateServiceSerializer, OrderSerializer, \
    CreateOrderSerializer, TagSerializer, CreateTagSerializer, OrderingSerializer, CreateOrderingSerializer, \
    MessageSerializer, CreateMessageSerializer, TicketSerializer, CreateTicketSerializer, ReviewSerializer, \
    AuthoringSerializer, CreateAuthoringSerializer


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class AssistantModelViewSet(viewsets.ModelViewSet):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer, CreateAssistantSerializer
    # permission_classes = (IsAssistant,)

    # def get_queryset(self):
    #     user = self.request.user

    #     if user.is_authenticated:
    #         return Assistant.objects.filter(user=user)

    #     raise PermissionDenied()

class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer, CreateClientSerializer


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer, CreateOrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()

        params = self.request.query_params

        service_type = params.get('service', None)
        client = params.get('client', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if client:
            queryset = queryset.filter(client__id=client)

        return queryset


class ServiceModelViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer, CreateServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()

        params = self.request.query_params

        service_type = params.get('service', None)
        assistant = params.get('assistant', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if assistant:
            queryset = queryset.filter(assistant__id=assistant)

        return queryset


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer, CreateTagSerializer


class OrderingModelViewSet(viewsets.ModelViewSet):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer, CreateOrderingSerializer


class MessageModelViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer, CreateMessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()

        params = self.request.query_params

        assistant = params.get('assistant', None)
        client = params.get('client', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)

        if assistant:
            queryset = queryset.filter(assistant__id=assistant)

        if client:
            queryset = queryset.filter(client__id=client)

        if from_date:
            queryset = queryset.filter(msg_date__gte=from_date)

        if to_date:
            queryset = queryset.filter(msg_date__lte=to_date)

        return queryset


class TicketModelViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer, CreateTicketSerializer


class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AuthoringModelViewSet(viewsets.ModelViewSet):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer, CreateAuthoringSerializer


