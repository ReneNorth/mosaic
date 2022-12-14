from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Count 
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from masterclass.models import Masterclass, MasterclassType
from booking.models import Booking
from blog.models import Post
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)
from rest_framework.permissions import AllowAny
from api.serializers import (MasterclassSerializer,
                             MasterclassTypeSerializer,
                             BookingSerializer, PostSerializer)


# мастерклассы - ридонли
# блоги - ридонли

# booking - чтение по своему аккаунту, запись, update, delete /
# все операции но с разными правами в зависимости от объекта


class MasterclassReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = MasterclassSerializer
    # queryset = Masterclass.objects.all()
    permission_classes = [AllowAny, ]
    
    def get_queryset(self):
        return Masterclass.objects.all().annotate(
            num_of_guests=Count('bookings__guest'))


class MasterclassTypeReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = MasterclassTypeSerializer
    queryset = MasterclassType.objects.all()
    permission_classes = [AllowAny, ]


class AbstractView(
    viewsets.GenericViewSet,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    pass


class BookingViewSet(AbstractView):
    """Viewset for user profile and course/masterclass bookings
    that process get, post and delete requests.
    Only authorized user can book a course. For non-authorized users there is
    a redirect to the 'call me back' page (or it will be done if not yet."""
    queryset = Booking.objects.all() # TODO после авторизации
    serializer_class = BookingSerializer
    # permission_classes = TODO


class PostReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PageNumberPagination
    # pagination_class = LimitOffsetPagination
