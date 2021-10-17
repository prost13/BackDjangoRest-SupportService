from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


class IsAssistant(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class AssistantRetrieveView(generics.RetrieveAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class AssistantUpdateView(generics.UpdateAPIView):
    queryset = Assistant.objects.all()
    serializer_class = CreateAssistantSerializer
    # permission_classes = (IsAssistant,)

    # def get_queryset(self):
    #     user = self.request.user

    #     if user.is_authenticated:
    #         return Assistant.objects.filter(user=user)

    #     raise PermissionDenied()


class AssistantCreateView(generics.CreateAPIView):
    queryset = Assistant.objects.all()
    serializer_class = CreateAssistantSerializer


class AssistantListView(generics.ListAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer


class ClientRetrieveView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

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


class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

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


class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class OrderingRetrieveView(generics.RetrieveAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class OrderingUpdateView(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderingCreateView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class OrderingListView(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class MessageListView(generics.ListAPIView):
    # queryset = Message.objects.all()
    serializer_class = MessageSerializer

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


class TicketRetrieveView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ReviewRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class AuthoringRetrieveView(generics.RetrieveAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer


class AuthoringUpdateView(generics.UpdateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringCreateView(generics.CreateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    # permission_class = permissions.IsAuthenticatedOrReadOnly


class AuthoringListView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer