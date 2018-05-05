from .models import Blog
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogs to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Custom_UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogs to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)    
    queryset = Custom_User.objects.all()
    serializer_class = Custom_UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogs to be viewed or edited.
    """
    permission_classes = (IsAdminUser,)    
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer

