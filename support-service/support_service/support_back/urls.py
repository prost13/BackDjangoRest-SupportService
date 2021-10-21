from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

from support_back import views

# urlpatterns = [
#     path('auth/', include('djoser.urls')),
#     # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     # path('auth/', include('rest_framework_social_oauth2.urls')),
#     path('auth/token/', obtain_auth_token, name='token'),
#     # path('auth/logout', Logout.as_view()),

router = DefaultRouter()
router.register(r'assistants', views.AssistantModelViewSet, basename='assistant')
router.register(r'clients', views.ClientModelViewSet, basename='client')
router.register(r'orders', views.OrderModelViewSet, basename='order')
router.register(r'services', views.ServiceModelViewSet, basename='service')
router.register(r'tags', views.TagModelViewSet, basename='tag')
router.register(r'orderings', views.OrderingModelViewSet, basename='ordering')
router.register(r'messages', views.MessageModelViewSet, basename='message')
router.register(r'tickets', views.TicketModelViewSet, basename='ticket')
router.register(r'reviews', views.ReviewModelViewSet, basename='review')
router.register(r'authorings', views.AuthoringModelViewSet, basename='authoring')
urlpatterns = router.urls

    # path('assistants/<int:pk>', AssistantRetrieveView.as_view()),
    # path('assistants/update/<int:pk>', AssistantUpdateView.as_view()),
    # path('assistants/all', AssistantListView.as_view()),
    # path('assistants/new', AssistantCreateView.as_view()),

    # path('clients/<int:pk>', ClientRetrieveView.as_view()),
    # path('clients/update/<int:pk>', ClientUpdateView.as_view()),
    # path('clients/all', ClientListView.as_view()),
    # path('clients/new', ClientCreateView.as_view()),
    #
    # path('orders/<int:pk>', OrderRetrieveView.as_view()),
    # path('orders/update/<int:pk>', OrderUpdateView.as_view()),
    # path('orders/all', OrderListView.as_view()),
    # path('orders/new', OrderCreateView.as_view()),
    #
    # path('services/<int:pk>', ServiceRetrieveView.as_view()),
    # path('services/update/<int:pk>', ServiceUpdateView.as_view()),
    # path('services/all', ServiceListView.as_view()),
    # path('services/new', ServiceCreateView.as_view()),
    #
    # path('tags/<int:pk>', TagRetrieveView.as_view()),
    # path('tags/update/<int:pk>', TagUpdateView.as_view()),
    # path('tags/all', TagListView.as_view()),
    # path('tags/new', TagCreateView.as_view()),
    #
    # path('orderings/<int:pk>', OrderingRetrieveView.as_view()),
    # path('orderings/update/<int:pk>', OrderingUpdateView.as_view()),
    # path('orderings/all', OrderingListView.as_view()),
    # path('orderings/new', OrderingCreateView.as_view()),
    #
    # path('messages/<int:pk>', MessageRetrieveView.as_view()),
    # path('messages/update/<int:pk>', MessageUpdateView.as_view()),
    # path('messages/all', MessageListView.as_view()),
    # path('messages/new', MessageCreateView.as_view()),
    #
    # path('tickets/<int:pk>', TicketRetrieveView.as_view()),
    # path('tickets/update/<int:pk>', TicketUpdateView.as_view()),
    # path('tickets/all', TicketListView.as_view()),
    # path('tickets/new', TicketCreateView.as_view()),
    #
    # path('reviews/<int:pk>', ReviewRetrieveUpdateView.as_view()),
    # path('reviews/update/<int:pk>', ReviewRetrieveUpdateView.as_view()),
    # path('reviews/all', ReviewListView.as_view()),
    # path('reviews/new', ReviewCreateView.as_view()),
    #
    # path('authorings/<int:pk>', AuthoringRetrieveView.as_view()),
    # path('authorings/update/<int:pk>', AuthoringUpdateView.as_view()),
    # path('authorings/all', AuthoringListView.as_view()),
    # path('authorings/new', AuthoringCreateView.as_view()),


